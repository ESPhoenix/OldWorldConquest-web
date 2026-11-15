#!/usr/bin/env python3
"""Build a low-rate, source-attributed Markdown reference archive.

Uses only URLs already listed in manifest.json. Resume by default; pass --refresh
to re-fetch and replace only those manifest destinations.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from urllib.parse import urljoin, urlparse, urlunparse
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup, NavigableString, Tag


ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = ROOT / "manifest.json"
USER_AGENT = "MordheimerOfflineReference/1.0 (personal reference archive)"
BASE_URL = "https://mordheimer.net/"
REQUEST_DELAY = 1.1
BR_TOKEN = "\ue000"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def save_manifest(manifest: dict) -> None:
    temp = MANIFEST_PATH.with_suffix(".json.tmp")
    temp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temp, MANIFEST_PATH)


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip("/"), "", "", ""))


def allowed_by_robots(session: requests.Session, url: str) -> bool:
    robots_url = urljoin(BASE_URL, "robots.txt")
    response = session.get(robots_url, timeout=30)
    response.raise_for_status()
    parser = RobotFileParser()
    parser.set_url(robots_url)
    parser.parse(response.text.splitlines())
    return parser.can_fetch(USER_AGENT, url)


def text_inline(node, page_url: str) -> str:
    if isinstance(node, NavigableString):
        return re.sub(r"\s+", " ", str(node))
    if not isinstance(node, Tag):
        return ""
    name = node.name.lower()
    if name in {"script", "style", "button", "svg"} or "hash-link" in node.get("class", []):
        return ""
    if name == "br":
        return BR_TOKEN
    if name == "img":
        alt = node.get("alt", "").strip()
        src = urljoin(page_url, node.get("src", ""))
        return f"![{alt}]({src})" if src else alt
    content = "".join(text_inline(child, page_url) for child in node.children)
    content = re.sub(r"\s+", " ", content).strip().replace(BR_TOKEN, "<br>")
    if name == "a":
        href = node.get("href")
        if href and content:
            return f"[{content}]({urljoin(page_url, href)})"
    if name in {"strong", "b"} and content:
        return f"**{content}**"
    if name in {"em", "i"} and content:
        return f"*{content}*"
    if name == "code" and content:
        return f"`{content}`"
    if name == "sup" and content:
        return f"^{content}"
    if name == "del" and content:
        return f"~~{content}~~"
    return content


def table_to_markdown(table: Tag, page_url: str) -> str:
    rows = []
    for tr in table.find_all("tr"):
        cells = tr.find_all(["th", "td"], recursive=False)
        if not cells:
            continue
        vals = []
        for cell in cells:
            value = text_inline(cell, page_url).replace("|", "\\|").strip()
            vals.append(value)
        rows.append(vals)
    if not rows:
        return ""
    width = max(map(len, rows))
    rows = [row + [""] * (width - len(row)) for row in rows]
    if table.find("th"):
        header = rows[0]
        body = rows[1:]
    else:
        header = rows[0]
        body = rows[1:]
    result = ["| " + " | ".join(header) + " |", "| " + " | ".join(["---"] * width) + " |"]
    result.extend("| " + " | ".join(row) + " |" for row in body)
    return "\n".join(result)


def list_to_markdown(list_tag: Tag, page_url: str, depth: int = 0) -> str:
    ordered = list_tag.name.lower() == "ol"
    lines = []
    number = int(list_tag.get("start", 1))
    for item in list_tag.find_all("li", recursive=False):
        prefix = f"{number}. " if ordered else "- "
        number += 1
        direct_parts = []
        nested_parts = []
        for child in item.children:
            if isinstance(child, Tag) and child.name.lower() in {"ul", "ol"}:
                nested_parts.append(list_to_markdown(child, page_url, depth + 1))
            elif isinstance(child, Tag) and child.name.lower() in {"p", "div"}:
                value = block_to_markdown(child, page_url).strip()
                if value:
                    direct_parts.append(value.replace("\n", " "))
            else:
                value = text_inline(child, page_url).strip()
                if value:
                    direct_parts.append(value)
        indent = "  " * depth
        lines.append(indent + prefix + " ".join(direct_parts))
        for nested in nested_parts:
            lines.extend(indent + "  " + line for line in nested.splitlines())
    return "\n".join(lines)


def block_to_markdown(node, page_url: str) -> str:
    if isinstance(node, NavigableString):
        value = re.sub(r"\s+", " ", str(node)).strip()
        return value
    if not isinstance(node, Tag):
        return ""
    name = node.name.lower()
    if name in {"script", "style", "nav", "button", "svg"}:
        return ""
    if name in {"strong", "b", "em", "i", "a", "span", "code", "sup", "del", "label"}:
        return text_inline(node, page_url).strip()
    if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        level = int(name[1])
        value = text_inline(node, page_url).strip()
        return f"{'#' * level} {value}" if value else ""
    if name == "p":
        return text_inline(node, page_url).strip()
    if name in {"ul", "ol"}:
        return list_to_markdown(node, page_url)
    if name == "table":
        return table_to_markdown(node, page_url)
    if name == "blockquote":
        body = "\n\n".join(filter(None, (block_to_markdown(c, page_url) for c in node.children))).strip()
        return "\n".join("> " + line for line in body.splitlines())
    if name == "pre":
        code = node.get_text("\n", strip=False).strip("\n")
        language = ""
        code_node = node.find("code")
        if code_node:
            classes = " ".join(code_node.get("class", []))
            match = re.search(r"language-([\w+-]+)", classes)
            if match:
                language = match.group(1)
        return f"```{language}\n{code}\n```"
    if name == "hr":
        return "---"
    if name == "details":
        return "\n\n".join(filter(None, (block_to_markdown(c, page_url) for c in node.children))).strip()
    if name == "summary":
        return f"**{text_inline(node, page_url).strip()}**"
    if name == "img":
        return text_inline(node, page_url)

    # Treat a div with only inline content as one paragraph. This preserves labels
    # and definitions used throughout weapon/armour entries instead of splitting
    # every inline element into separate Markdown paragraphs.
    if name == "div" and not node.find(["p", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "table", "blockquote", "pre"]):
        value = text_inline(node, page_url).strip()
        value = re.sub(r"(\*\*[^*\n]+?)\s+(:\*\*)", r"\1\2", value)
        return re.sub(r"(\*\*[^*\n]+\*\*)(?=\S)", r"\1 ", value)

    # Recurse through article containers and admonitions while preserving blocks.
    chunks = []
    for child in node.children:
        rendered = block_to_markdown(child, page_url).strip()
        if rendered:
            chunks.append(rendered)
    if chunks:
        return "\n\n".join(chunks)
    return text_inline(node, page_url).strip()


def localize_links(markdown: str, source_path: PurePosixPath, path_by_url: dict[str, str]) -> str:
    def replace(match: re.Match) -> str:
        label, url = match.group(1), match.group(2)
        parsed = urlparse(url)
        if parsed.netloc not in {"", "mordheimer.net", "www.mordheimer.net"}:
            return match.group(0)
        target = normalize_url(urljoin(BASE_URL, url))
        target_path = path_by_url.get(target)
        if not target_path:
            return match.group(0)
        relative = os.path.relpath(target_path, str(source_path.parent)).replace(os.sep, "/")
        suffix = f"#{parsed.fragment}" if parsed.fragment else ""
        return f"[{label}]({relative}{suffix})"

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace, markdown)


def make_page(entry: dict, html: str, fetched_at: str, path_by_url: dict[str, str]) -> str:
    soup = BeautifulSoup(html, "html.parser")
    article = soup.select_one(".theme-doc-markdown") or soup.find("article") or soup.find("main")
    if not article:
        raise ValueError("Could not find the documentation article body")
    # Exclude interactive warband filters/dropdowns; they are navigation UI, not
    # part of the rules text, and their options otherwise pollute the article.
    for control in article.select("select, input, button, [role=combobox]"):
        container = control.find_parent(class_="box") or control.parent
        if container:
            container.decompose()
    rendered = block_to_markdown(article, entry["source_url"])
    rendered = re.sub(r"(?:<br>\s*){2,}", "\n\n", rendered)
    rendered = re.sub(r"\n{3,}", "\n\n", rendered).strip()
    rendered = re.sub(r"\*{4,}([^*]+)\*{4,}", r"***\1***", rendered)
    if len(re.sub(r"\s", "", rendered)) < 100:
        raise ValueError("Extracted article looks unexpectedly short; refusing to save")

    page_path = PurePosixPath(entry["local_path"])
    rendered = localize_links(rendered, page_path, path_by_url)
    match = re.search(r"Last updated on\s+(.+?)\s*(?:\n|$)", soup.get_text("\n", strip=True), re.I)
    site_updated = match.group(1).strip(" *") if match else ""
    grade = entry.get("grade", "")
    source = ""  # Original in-page citations remain in the article body.
    fields = [
        f'title: {json.dumps(entry["title"], ensure_ascii=False)}',
        f'source_url: {json.dumps(entry["source_url"], ensure_ascii=False)}',
        f'fetched_at: {json.dumps(fetched_at)}',
        f'section: {json.dumps(entry.get("section", ""))}',
    ]
    if grade:
        fields.append(f'grade: {json.dumps(grade)}')
    if site_updated:
        fields.append(f'site_last_updated: {json.dumps(site_updated, ensure_ascii=False)}')
    if source:
        fields.append(f'source: {json.dumps(source, ensure_ascii=False)}')
    return "---\n" + "\n".join(fields) + "\n---\n\n" + rendered + "\n"


def write_indexes(entries: list[dict]) -> None:
    def link(entry: dict, from_path: str) -> str:
        rel = os.path.relpath(entry["local_path"], str(PurePosixPath(from_path).parent)).replace(os.sep, "/")
        return f"- [{entry['title']}]({rel}) ([source](<{entry['source_url']}>))"

    sections = {
        "core-rules": [e for e in entries if e.get("section") == "core-rules"],
        "skills": [e for e in entries if e.get("section") == "skills"],
        "weapons-armour": [e for e in entries if e.get("section") == "weapons-armour"],
    }
    for section, items in sections.items():
        index = f"{section}/index.md"
        title = {"core-rules": "Core rules", "skills": "Skills", "weapons-armour": "Weapons and armour"}[section]
        body = f"# {title} — offline index\n\n" + "\n".join(link(e, index) for e in items)
        (ROOT / index).write_text(body + "\n", encoding="utf-8")

    grade_titles = {"1a": "Grade 1A", "1b": "Grade 1B", "1c": "Grade 1C"}
    for grade, title in grade_titles.items():
        items = [e for e in entries if e.get("grade") == grade]
        index = f"warbands/grade-{grade}/index.md"
        body = f"# {title} warbands — offline index\n\n" + "\n".join(link(e, index) for e in items)
        (ROOT / index).write_text(body + "\n", encoding="utf-8")

    warband_index = "warbands/index.md"
    body = "# Warbands — offline index\n\n- [Starting a Warband](starting-a-warband.md)\n" + "\n".join(
        f"- [{grade_titles[g]}](grade-{g}/index.md)" for g in grade_titles
    )
    (ROOT / warband_index).write_text(body + "\n", encoding="utf-8")

    root_index = "index.md"
    body = "# Mordheimer offline reference archive\n\n"
    body += "- [Core rules](core-rules/index.md)\n- [Warbands](warbands/index.md)\n"
    body += "- [Weapons and armour](weapons-armour/index.md)\n- [Skills](skills/index.md)\n"
    if any(entry.get("section") == "campaigns" for entry in entries):
        body += "- [Campaigns](campaigns/index.md)\n"
    body += "- [Source manifest](manifest.json)\n\n"
    body += "Local reference copy; see [README](README.md) for provenance and rights/access notes.\n"
    (ROOT / root_index).write_text(body, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="re-fetch and replace manifest destination files")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    entries = manifest["sources"]
    path_by_url = {normalize_url(e["source_url"]): e["local_path"] for e in entries}
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"})

    try:
        if not allowed_by_robots(session, BASE_URL):
            print("robots.txt does not permit this crawler; stopping without fetching pages.", file=sys.stderr)
            return 2
    except requests.RequestException as exc:
        print(f"Could not verify robots.txt ({exc}); stopping without fetching pages.", file=sys.stderr)
        return 2

    total = len(entries)
    failed = []
    for index, entry in enumerate(entries, 1):
        destination = ROOT / entry["local_path"]
        if destination.exists() and not args.refresh:
            print(f"[{index}/{total}] exists, skip: {entry['local_path']}")
            if entry.get("status") != "downloaded":
                entry["status"] = "downloaded"
                entry["notes"] = "Local file already existed; not overwritten."
                save_manifest(manifest)
            continue

        print(f"[{index}/{total}] fetch: {entry['source_url']}", flush=True)
        if index > 1:
            time.sleep(REQUEST_DELAY)
        response = None
        for attempt in range(3):
            try:
                response = session.get(entry["source_url"], timeout=30)
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
                if attempt == 2:
                    entry["status"] = "error"
                    entry["notes"] = str(exc)
                    failed.append(entry["source_url"])
                    save_manifest(manifest)
                    response = None
                    break
                time.sleep(2 ** attempt)
        if response is None:
            continue

        fetched_at = utc_now()
        try:
            markdown = make_page(entry, response.text, fetched_at, path_by_url)
        except Exception as exc:
            entry["status"] = "error"
            entry["notes"] = f"Extraction error: {exc}"
            failed.append(entry["source_url"])
            save_manifest(manifest)
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(markdown, encoding="utf-8")
        entry["status"] = "downloaded"
        entry["fetched_at"] = fetched_at
        entry["site_last_updated"] = next(
            (line.split(": ", 1)[1] for line in markdown.splitlines() if line.startswith("site_last_updated: ")), None
        )
        entry["sha256"] = hashlib.sha256(markdown.encode("utf-8")).hexdigest()
        entry["notes"] = ""
        save_manifest(manifest)

    write_indexes(entries)
    if failed:
        print(f"Completed with {len(failed)} failed page(s); see manifest.json.", file=sys.stderr)
        return 1
    manifest["catalog_status"] = "downloaded"
    manifest["content_copied"] = True
    save_manifest(manifest)
    print(f"Done: processed {total} source entries. See index.md.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(f"Stopped safely: {exc}", file=sys.stderr)
        raise SystemExit(2)
