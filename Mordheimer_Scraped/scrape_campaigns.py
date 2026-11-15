#!/usr/bin/env python3
"""Discover and archive the complete /docs/campaigns subtree, at a low request rate."""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import quote, unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from scrape import (
    BASE_URL,
    REQUEST_DELAY,
    ROOT,
    USER_AGENT,
    allowed_by_robots,
    make_page,
    normalize_url,
    save_manifest,
    utc_now,
)


CACHE_DIR = ROOT / ".campaign-scrape-cache"
STATE_PATH = CACHE_DIR / "state.json"
MANIFEST_PATH = ROOT / "manifest.json"
CAMPAIGN_PREFIX = "/docs/campaigns"


def canonical_route(url: str) -> str | None:
    parsed = urlparse(urljoin(BASE_URL, url))
    if parsed.netloc not in {"mordheimer.net", "www.mordheimer.net"}:
        return None
    path = unquote(parsed.path).rstrip("/") or "/"
    if path != CAMPAIGN_PREFIX and not path.startswith(CAMPAIGN_PREFIX + "/"):
        return None
    return path


def route_url(route: str) -> str:
    return "https://mordheimer.net" + quote(route, safe="/-._~")


def cache_path(route: str) -> Path:
    digest = hashlib.sha256(route.encode("utf-8")).hexdigest()[:24]
    return CACHE_DIR / f"{digest}.html"


def write_state(state: dict) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    temp = STATE_PATH.with_suffix(".json.tmp")
    temp.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(STATE_PATH)


def discover_links(html: str, page_url: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    found = set()
    for link in soup.select("a[href]"):
        route = canonical_route(urljoin(page_url, link.get("href", "")))
        if route:
            found.add(route)
    return sorted(found)


def get_title(html: str, route: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    heading = soup.select_one(".theme-doc-markdown h1") or soup.select_one("article h1")
    if heading:
        return heading.get_text(" ", strip=True)
    if soup.title:
        return soup.title.get_text(" ", strip=True).split(" | ", 1)[0]
    return route.rsplit("/", 1)[-1].replace("-", " ").title()


def local_path_for(route: str) -> str:
    if route == CAMPAIGN_PREFIX:
        return "campaigns/campaigns-overview.md"
    suffix = route[len(CAMPAIGN_PREFIX):].strip("/")
    parts = [re.sub(r"[^a-z0-9-]", "", re.sub(r"\s+", "-", part.lower())) for part in suffix.split("/")]
    return "campaigns/" + "/".join(parts) + ".md"


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def generate_campaign_index(manifest: dict) -> None:
    entries = [item for item in manifest["sources"] if item.get("section") == "campaigns"]
    by_path = {Path(item["local_path"]).as_posix(): item for item in entries}
    folders = {"campaigns"}
    for item in entries:
        parent = Path(item["local_path"]).parent
        while str(parent) != ".":
            folders.add(parent.as_posix())
            parent = parent.parent

    for folder in sorted(folders, key=lambda value: (value.count("/"), value)):
        folder_path = Path(folder)
        lines = [f"# {folder_path.name.replace('-', ' ').title()} — offline index", ""]
        children = []
        for relative_path, item in by_path.items():
            file_path = Path(relative_path)
            if file_path.parent == folder_path:
                children.append((item["title"].casefold(), item["title"], file_path.name))
        for child_folder in folders:
            child_path = Path(child_folder)
            if child_path.parent == folder_path and child_path.name != ".":
                title = child_path.name.replace('-', ' ').title()
                children.append((f"browse {title}".casefold(), f"Browse {title}", f"{child_path.name}/index.md"))
        for _, title, child in sorted(children):
            lines.append(f"- [{title}]({child})")
        if folder == "campaigns":
            lines.append("- [Standard Skills](../skills/standard-skills.md)")
        destination = ROOT / folder_path / "index.md"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text("\n".join(lines) + "\n", encoding="utf-8")

    index_path = ROOT / "index.md"
    index_text = index_path.read_text(encoding="utf-8")
    if "[Campaigns](campaigns/index.md)" not in index_text:
        index_text = index_text.replace("- [Skills](skills/index.md)\n", "- [Skills](skills/index.md)\n- [Campaigns](campaigns/index.md)\n")
        index_path.write_text(index_text, encoding="utf-8")


def main() -> int:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest()
    existing = {normalize_url(item["source_url"]): item for item in manifest["sources"]}
    if STATE_PATH.exists():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    else:
        state = {"pending": [CAMPAIGN_PREFIX], "pages": {}}
        write_state(state)

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"})
    try:
        if not allowed_by_robots(session, route_url(CAMPAIGN_PREFIX)):
            print("robots.txt does not permit this crawler; stopping.", file=sys.stderr)
            return 2
    except requests.RequestException as exc:
        print(f"Could not verify robots.txt ({exc}); stopping: {exc}", file=sys.stderr)
        return 2

    while state["pending"]:
        route = state["pending"].pop(0)
        if route in state["pages"]:
            write_state(state)
            continue
        source_url = route_url(route)
        existing_item = existing.get(normalize_url(source_url))
        if existing_item:
            state["pages"][route] = {"status": "already-archived", "local_path": existing_item["local_path"]}
            write_state(state)
            continue

        print(f"Discover/fetch {route}", flush=True)
        if state.get("requested_count", 0):
            time.sleep(REQUEST_DELAY)
        response = None
        for attempt in range(3):
            try:
                response = session.get(source_url, timeout=30)
                if response.status_code == 429:
                    raise RuntimeError("HTTP 429 rate limit; stopping to respect server limits")
                if response.status_code >= 500 and attempt < 2:
                    time.sleep(2 ** attempt)
                    continue
                response.raise_for_status()
                break
            except RuntimeError:
                raise
            except requests.RequestException as exc:
                if response is not None and response.status_code == 404:
                    state["pages"][route] = {"status": "not-found", "error": str(exc)}
                    write_state(state)
                    response = None
                    break
                if attempt == 2:
                    state["pages"][route] = {"status": "error", "error": str(exc)}
                    write_state(state)
                    print(f"Failed {route}: {exc}", file=sys.stderr)
                    response = None
                    break
                time.sleep(2 ** attempt)
        state["requested_count"] = state.get("requested_count", 0) + 1
        if response is None:
            write_state(state)
            continue

        html = response.text
        file_path = cache_path(route)
        file_path.write_text(html, encoding="utf-8")
        state["pages"][route] = {
            "status": "fetched",
            "cache_file": file_path.name,
            "fetched_at": utc_now(),
            "title": get_title(html, route),
        }
        for discovered in discover_links(html, source_url):
            if discovered not in state["pages"] and discovered not in state["pending"]:
                state["pending"].append(discovered)
        write_state(state)

    fetched = [
        (route, record)
        for route, record in state["pages"].items()
        if record.get("status") == "fetched"
    ]
    path_by_url = {normalize_url(item["source_url"]): item["local_path"] for item in manifest["sources"]}
    additions = []
    for route, record in sorted(fetched):
        source_url = route_url(route)
        local_path = local_path_for(route)
        entry = {
            "title": record["title"],
            "section": "campaigns",
            "source_url": source_url,
            "local_path": local_path,
            "status": "pending",
            "fetched_at": None,
            "site_last_updated": None,
            "sha256": None,
            "notes": "",
        }
        additions.append(entry)
        path_by_url[normalize_url(source_url)] = local_path

    known_paths = {item["local_path"] for item in manifest["sources"]}
    additions = [item for item in additions if item["local_path"] not in known_paths]
    manifest["sources"].extend(additions)
    save_manifest(manifest)
    fetched_routes = {route for route, _ in fetched}
    to_convert = list(additions)
    for entry in manifest["sources"]:
        route = urlparse(entry["source_url"]).path.rstrip("/")
        record = state["pages"].get(route, {})
        if route in fetched_routes and entry not in to_convert and entry.get("status") != "downloaded" and record.get("status") == "fetched":
            to_convert.append(entry)
    path_by_url = {normalize_url(item["source_url"]): item["local_path"] for item in manifest["sources"]}
    print(f"Converting {len(to_convert)} campaign pages to Markdown.", flush=True)

    for entry in to_convert:
        route = urlparse(entry["source_url"]).path.rstrip("/")
        record = state["pages"][route]
        html = (CACHE_DIR / record["cache_file"]).read_text(encoding="utf-8")
        fetched_at = record["fetched_at"]
        try:
            markdown = make_page(entry, html, fetched_at, path_by_url)
        except Exception as exc:
            if route.startswith(("/docs/campaigns/hired-swords/grade-", "/docs/campaigns/dramatis-personae/grade-")):
                related = "core.md"
                category = "Hired Swords" if "/hired-swords/" in route else "Dramatis Personae"
                sibling = "hired-swords" if category == "Hired Swords" else "dramatis-personae"
                related_path = f"campaigns/{sibling}/{related}"
                relative = os.path.relpath(related_path, str(Path(entry["local_path"]).parent)).replace(os.sep, "/")
                markdown = (
                    "---\n"
                    f'title: {json.dumps(entry["title"], ensure_ascii=False)}\n'
                    f'source_url: {json.dumps(entry["source_url"], ensure_ascii=False)}\n'
                    f'fetched_at: {json.dumps(fetched_at)}\n'
                    'section: "campaigns"\n'
                    "---\n\n"
                    f"# {entry['title']}\n\n"
                    "The source route renders a client-side warband filter; its server-delivered article contains no entry descriptions to archive. "
                    f"See the available [{category} rules]({relative}) and the [Campaigns index](../index.md).\n"
                )
                entry["notes"] = "Source route is a client-side filter with no rule-entry text in the delivered article; see linked category listing."
            else:
                entry["status"] = "error"
                entry["notes"] = f"Extraction error: {exc}"
                save_manifest(manifest)
                print(f"Extraction failed for {route}: {exc}", file=sys.stderr)
                continue
        destination = ROOT / entry["local_path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(markdown, encoding="utf-8")
        entry["status"] = "downloaded"
        entry["fetched_at"] = fetched_at
        entry["sha256"] = hashlib.sha256(markdown.encode("utf-8")).hexdigest()
        save_manifest(manifest)

    generate_campaign_index(manifest)
    errors = [entry for entry in to_convert if entry.get("status") != "downloaded"]
    if errors:
        print(f"Campaign scrape completed with {len(errors)} conversion error(s); cache retained for recovery.", file=sys.stderr)
        return 1

    # The Markdown files and manifest are now the archive; remove only this
    # script's temporary response cache to avoid a second copy of the content.
    for cache_file in CACHE_DIR.glob("*.html"):
        cache_file.unlink()
    if STATE_PATH.exists():
        STATE_PATH.unlink()
    try:
        CACHE_DIR.rmdir()
    except OSError:
        pass
    print(f"Campaign archive complete: {len(additions)} new pages; run `python linkify.py` next.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(f"Stopped safely: {exc}", file=sys.stderr)
        raise SystemExit(2)
