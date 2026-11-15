#!/usr/bin/env python3
"""Add local links for rule, skill, weapon, and armour references in archive pages."""

from __future__ import annotations

import json
import hashlib
import os
import re
import unicodedata
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlparse, urlunparse


ROOT = Path(__file__).resolve().parent
MANIFEST = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
SOURCES = {item["local_path"]: item for item in MANIFEST["sources"]}
CONTENT_PATHS = set(SOURCES)


def slugify(heading: str) -> str:
    value = unicodedata.normalize("NFKD", heading).encode("ascii", "ignore").decode().lower()
    value = re.sub(r"[`*_~]", "", value)
    value = re.sub(r"[^a-z0-9_ -]", "", value)
    # GitHub/Docusaurus-style heading slugs preserve repeated spaces as repeated
    # hyphens (notably headings written as "0 – 1 ...").
    return value.replace(" ", "-").strip("-")


def rel_link(source: str, target: str, anchor: str) -> str:
    path = os.path.relpath(target, str(PurePosixPath(source).parent)).replace(os.sep, "/")
    return f"{path}#{anchor}" if anchor else path


def headings(path: str) -> list[tuple[int, str, str]]:
    text = (ROOT / path).read_text(encoding="utf-8")
    result = []
    in_frontmatter = False
    saw_frontmatter = False
    for line in text.splitlines():
        if line.strip() == "---" and not saw_frontmatter:
            in_frontmatter = not in_frontmatter
            if not in_frontmatter:
                saw_frontmatter = True
            continue
        if in_frontmatter:
            continue
        match = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if match:
            title = match.group(2).strip()
            result.append((len(match.group(1)), title, slugify(title)))
    return result


def make_target_map() -> dict[str, tuple[str, str]]:
    targets: dict[str, tuple[str, str]] = {}

    def add(term: str, path: str, anchor: str, *, replace: bool = False) -> None:
        term = re.sub(r"\s+", " ", term.strip())
        if not term:
            return
        key = term.casefold()
        if replace or key not in targets:
            targets[key] = (path, anchor)

    # Weapon, armour, and equipment entries are canonical in the armoury pages.
    for path, item in SOURCES.items():
        if item.get("section") != "weapons-armour" or path.endswith("index.md"):
            continue
        for level, title, anchor in headings(path):
            if level < 3 or title.casefold() in {"special rules", "weapons, armour & equipment"}:
                continue
            add(title, path, anchor)

    # Common alternate labels and individual items covered by a combined entry.
    aliases = {
        "Hammer": "weapons-armour/close-combat.md#hammer-staff-mace-or-club",
        "Staff": "weapons-armour/close-combat.md#hammer-staff-mace-or-club",
        "Mace": "weapons-armour/close-combat.md#hammer-staff-mace-or-club",
        "Club": "weapons-armour/close-combat.md#hammer-staff-mace-or-club",
        "Duelling pistol": "weapons-armour/blackpowder.md#duelling-pistol",
        "Dueling pistol": "weapons-armour/blackpowder.md#duelling-pistol",
        "Double handed weapon": "weapons-armour/close-combat.md#double-handed-weapon",
        "Double-handed weapons": "weapons-armour/close-combat.md#double-handed-weapon",
        "Throwing knife": "weapons-armour/missile.md#throwing-knivesstars",
        "Throwing knives": "weapons-armour/missile.md#throwing-knivesstars",
        "Throwing star": "weapons-armour/missile.md#throwing-knivesstars",
        "Throwing stars": "weapons-armour/missile.md#throwing-knivesstars",
        "Weeping blade": "weapons-armour/close-combat.md#weeping-blades",
        "Weeping blade(s)": "weapons-armour/close-combat.md#weeping-blades",
        "Light armor": "weapons-armour/armour.md#light-armour",
        "Heavy armor": "weapons-armour/armour.md#heavy-armour",
        "Ithilmar armor": "weapons-armour/armour.md#ithilmar-armour",
        "Gromril armor": "weapons-armour/armour.md#gromril-armour",
        "armor": "weapons-armour/armour.md#armour",
        "armour": "weapons-armour/armour.md#armour",
        "crossbow pistol": "weapons-armour/missile.md#crossbow-pistol",
        "Crossbow pistols": "weapons-armour/missile.md#crossbow-pistol",
    }
    for term, value in aliases.items():
        target_path, anchor = value.split("#", 1)
        add(term, target_path, anchor, replace=term.casefold() in {"armor", "armour"})

    # Add straightforward plural forms for armor/weapons headings.
    for term, (path, anchor) in list(targets.items()):
        if term.casefold() in {"staff", "fish-hook shot"}:
            continue
        if not term.casefold().endswith("s") and len(term) > 3:
            plural = term + "s"
            if plural.casefold() not in {key.casefold() for key in targets}:
                add(plural, path, anchor)

    # Items in warband equipment tables that do not have a standalone armoury
    # entry link to their originating equipment-list subsection.
    category_aliases = {
        "hand-to-hand combat weapons": "hand-to-hand-combat-weapons",
        "hand to hand combat weapons": "hand-to-hand-combat-weapons",
        "missile weapons": "missile-weapons",
        "armour": "armour",
    }
    for path, item in SOURCES.items():
        if item.get("section") != "warbands" or path.endswith("index.md"):
            continue
        lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
        current_category = ""
        index = 0
        while index < len(lines):
            line = lines[index]
            heading = re.match(r"^#{2,6}\s+(.+?)\s*#*\s*$", line)
            if heading:
                title = heading.group(1).strip()
                normalized = re.sub(r"\s+", " ", title.casefold())
                current_category = slugify(title) if normalized in category_aliases else ""
                index += 1
                continue
            if not current_category or not line.startswith("|"):
                index += 1
                continue
            table = []
            while index < len(lines) and lines[index].startswith("|"):
                table.append([cell.strip() for cell in lines[index].strip().strip("|").split("|")])
                index += 1
            if not table or len(table[0]) < 2:
                continue
            header = [cell.casefold() for cell in table[0]]
            if header[0] not in {"item", "weapon"} or "cost" not in header:
                continue
            for cells in table[2:]:
                if len(cells) < 2:
                    continue
                item_name = re.sub(r"[✏️❓*]", "", cells[0]).strip()
                item_name = re.sub(r"\s+", " ", item_name)
                if not item_name or item_name.casefold() in {"none", "item", "weapon"}:
                    continue
                if item_name.casefold() in {key.casefold() for key in targets}:
                    continue
                add(item_name, path, current_category)

    # Core-rule chapter names and section headings.
    generic = {
        "phases", "armour", "injuries", "terrain", "moving", "range", "leaders",
        "heroes", "henchmen", "zero level characteristics", "characteristic profiles",
    }
    for path, item in SOURCES.items():
        if path.startswith("core-rules/rules/") and path != "core-rules/rules/index.md":
            for level, title, anchor in headings(path):
                if level == 1:
                    add(title, path, anchor)
                    continue
                if title.casefold() in generic:
                    continue
                add(title, path, anchor)

    # Link each standard skill to its definition page as a rules reference.
    skill_path = "skills/standard-skills.md"
    for level, title, anchor in headings(skill_path):
        if level >= 3:
            add(title, skill_path, anchor)

    # Useful wording variants for frequently cited rules.
    rule_aliases = {
        "hand-to-hand combat": ("core-rules/rules/close-combat.md", "who-can-fight"),
        "hand to hand combat": ("core-rules/rules/close-combat.md", "who-can-fight"),
        "close-combat": ("core-rules/rules/close-combat.md", "who-can-fight"),
        "close combat": ("core-rules/rules/close-combat.md", "who-can-fight"),
        "shooting phase": ("core-rules/rules/shooting.md", "who-can-shoot"),
        "movement phase": ("core-rules/rules/movement.md", "moving"),
        "recovery phase": ("core-rules/rules/recovery.md", "recovery-phase"),
        "rout test": ("core-rules/rules/leadership-psychology.md", "the-rout-test"),
        "rout tests": ("core-rules/rules/leadership-psychology.md", "the-rout-test"),
        "all alone test": ("core-rules/rules/leadership-psychology.md", "all-alone"),
        "all alone tests": ("core-rules/rules/leadership-psychology.md", "all-alone"),
        "wound chart": ("core-rules/rules/close-combat.md", "wound-chart"),
        "critical hit chart": ("core-rules/rules/close-combat.md", "critical-hit-chart"),
        "critical hits": ("core-rules/rules/shooting.md", "critical-hits"),
        "critical hit": ("core-rules/rules/shooting.md", "critical-hits"),
        "armour save": ("core-rules/rules/close-combat.md", "armour"),
        "armour save modifiers": ("core-rules/rules/close-combat.md", "armour-save-modifiers"),
        "weapon modifiers": ("core-rules/rules/close-combat.md", "weapon-modifiers"),
        "knocked down": ("core-rules/rules/wounds-and-injuries.md", "warriors-knocked-down"),
        "stunned": ("core-rules/rules/wounds-and-injuries.md", "warriors-stunned"),
        "characteristic test": ("core-rules/rules/characteristics.md", "characteristic-tests"),
        "leadership test": ("core-rules/rules/characteristics.md", "leadership-tests"),
    }
    for term, (path, anchor) in rule_aliases.items():
        add(term, path, anchor, replace=term.casefold() in {"armour save", "armour save modifiers"})

    # Campaign rules and scenario/document titles are useful local destinations
    # for cross-references from other campaign pages.
    campaign_generic = {
        "special rules", "special skills", "heroes", "henchmen", "choice of warriors",
        "starting experience", "equipment list", "weapons and armour", "armour",
    }
    campaign_single_terms = {
        "campaigns", "experience", "income", "trading", "scenarios", "exploration",
        "campaign settings", "serious injuries", "hired swords", "dramatis personae",
        "warband rating", "post battle sequence", "freelancer",
    }
    for path, item in SOURCES.items():
        if item.get("section") != "campaigns":
            continue
        for level, title, anchor in headings(path):
            normalized = re.sub(r"\s+", " ", title.casefold())
            if normalized in campaign_generic:
                continue
            if level == 1 or len(normalized.split()) >= 2 or normalized in campaign_single_terms:
                add(title, path, anchor)

    preferred_campaign_destinations = {
        "campaigns": ("campaigns/campaigns-overview.md", "campaigns"),
        "experience": ("campaigns/experience.md", "experience"),
        "income": ("campaigns/income.md", "income"),
        "trading": ("campaigns/trading.md", "trading"),
        "scenarios": ("campaigns/scenarios.md", "scenarios"),
        "hired swords": ("campaigns/hired-swords.md", "hired-swords"),
        "dramatis personae": ("campaigns/dramatis-personae.md", "dramatis-personae"),
        "campaign settings": ("campaigns/campaign-settings.md", "campaign-settings"),
        "freelancer": ("campaigns/hired-swords/core.md", "freelancer"),
        "warband rating": ("campaigns/campaigns-overview.md", "warband-rating"),
        "post battle sequence": ("campaigns/campaigns-overview.md", "post-battle-sequence"),
    }
    for term, (path, anchor) in preferred_campaign_destinations.items():
        add(term, path, anchor, replace=True)

    # Named specialist gear that appears only in a warband's starting-equipment
    # text, with no standalone item entry in the shared armoury.
    add("masterwork heavy armour", "weapons-armour/armour.md", "heavy-armour", replace=True)
    add("bec de corbin", "weapons-armour/close-combat.md", "close-combat-weapons", replace=True)
    add("firepots miragliano", "warbands/grade-1c/lustrian-reavers.md", "special-equipment", replace=True)
    add("firepots", "warbands/grade-1c/lustrian-reavers.md", "special-equipment", replace=True)

    return targets


def linkify_text(text: str, source: str, targets: dict[str, tuple[str, str]]) -> tuple[str, int]:
    # Protect existing links, inline code, raw URLs, and HTML tags so the pass is
    # idempotent and does not corrupt destinations or markup.
    protected = re.compile(r"(!?\[[^\]]*\]\([^)]*\)|`[^`]*`|https?://[^\s)>]+|<[^>]+>)")
    parts = []
    cursor = 0
    links_added = 0
    for match in protected.finditer(text):
        plain = text[cursor:match.start()]
        plain, count = apply_terms(plain, source, targets)
        parts.append(plain)
        parts.append(match.group(0))
        links_added += count
        cursor = match.end()
    plain, count = apply_terms(text[cursor:], source, targets)
    parts.append(plain)
    return "".join(parts), links_added + count


def apply_terms(text: str, source: str, targets: dict[str, tuple[str, str]]) -> tuple[str, int]:
    if not text:
        return text, 0
    terms = sorted(targets, key=lambda term: (-len(term), term.casefold()))
    pattern = re.compile(r"(?<![\w])(?:" + "|".join(re.escape(term) for term in terms) + r")(?![\w])", re.I)
    count = 0

    def replace(match: re.Match) -> str:
        nonlocal count
        term = match.group(0)
        target_path, anchor = targets[term.casefold()]
        count += 1
        return f"[{term}]({rel_link(source, target_path, anchor)})"

    return pattern.sub(replace, text), count


def repair_local_anchors(targets: dict[str, tuple[str, str]]) -> int:
    """Normalize existing local fragments to anchors present in local Markdown."""
    files = sorted(ROOT.rglob("*.md"))
    anchor_cache: dict[str, set[str]] = {}
    repair_count = 0
    link_pattern = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")

    def compact(value: str) -> str:
        return re.sub(r"[^a-z0-9]", "", value.casefold())

    def root_anchor(path: str) -> str:
        page_headings = headings(path)
        return next((slug for level, _, slug in page_headings if level == 1), page_headings[0][2] if page_headings else "")

    for source_file in files:
        source = source_file.relative_to(ROOT).as_posix()
        original = source_file.read_text(encoding="utf-8")

        def replace(match: re.Match) -> str:
            nonlocal repair_count
            label, raw_target = match.group(1), match.group(2)
            target = raw_target.strip("<>")
            if target.startswith(("http://", "https://", "mailto:")):
                return match.group(0)
            target_path, marker, anchor = target.partition("#")
            destination = (source_file.parent / target_path).resolve() if target_path else source_file
            try:
                target_relative = destination.relative_to(ROOT).as_posix()
            except ValueError:
                return match.group(0)
            if not destination.is_file() or not marker:
                return match.group(0)
            if target_relative not in anchor_cache:
                anchor_cache[target_relative] = {slug for _, _, slug in headings(target_relative)}
            available = anchor_cache[target_relative]

            label_key = re.sub(r"[*_`]", "", label).casefold()
            preferred_terms = {
                "campaigns", "experience", "income", "trading", "scenarios", "hired swords",
                "dramatis personae", "campaign settings", "warband rating", "post battle sequence",
            }
            preferred = targets.get(label_key) if label_key in preferred_terms else None
            if preferred:
                preferred_path, preferred_anchor = preferred
                if target_relative != preferred_path or anchor != preferred_anchor:
                    resolved_file = ROOT / preferred_path
                    if preferred_path not in anchor_cache:
                        anchor_cache[preferred_path] = {slug for _, _, slug in headings(preferred_path)}
                    if preferred_anchor in anchor_cache[preferred_path]:
                        repair_count += 1
                        return f"[{label}]({rel_link(source, preferred_path, preferred_anchor)})"
            if anchor in available:
                return match.group(0)

            # Prefer a heading whose normalized text matches the old fragment;
            # this repairs differences such as Docusaurus' `doublehanded` slug.
            match_anchor = next((candidate for candidate in available if compact(candidate) == compact(anchor)), None)
            if match_anchor:
                new_target = f"{target_path}#{match_anchor}"
            else:
                # Some source links point to a named equipment row rather than
                # an actual heading. Redirect those to the closest local entry.
                resolved = targets.get(re.sub(r"[*_`]", "", label).casefold())
                if resolved:
                    resolved_path, resolved_anchor = resolved
                    if resolved_path not in anchor_cache:
                        anchor_cache[resolved_path] = {slug for _, _, slug in headings(resolved_path)}
                    if resolved_anchor not in anchor_cache[resolved_path]:
                        # No item-specific heading exists in the target page; keep
                        # the cross-reference useful by linking to its section title.
                        resolved_anchor = root_anchor(resolved_path)
                    if resolved_anchor:
                        new_target = rel_link(source, resolved_path, resolved_anchor)
                    else:
                        fallback = root_anchor(target_relative)
                        new_target = f"{target_path}#{fallback}" if fallback else target_path
                else:
                    # Preserve a valid destination even when the source site's
                    # fragment points to an item row that is not a local heading.
                    fallback = root_anchor(target_relative)
                    new_target = f"{target_path}#{fallback}" if fallback else target_path
            repair_count += 1
            return f"[{label}]({new_target})"

        updated = link_pattern.sub(replace, original)
        if updated != original:
            source_file.write_text(updated, encoding="utf-8")
    return repair_count


def localize_in_scope_links() -> int:
    """Rewrite archived Mordheimer links to local files where a copy exists."""
    path_by_url: dict[str, str] = {}
    for item in MANIFEST["sources"]:
        parsed = urlparse(item["source_url"])
        base = urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip("/"), "", "", ""))
        path_by_url[base] = item["local_path"]
        decoded = urlunparse((parsed.scheme, parsed.netloc, unquote(parsed.path).rstrip("/"), "", "", ""))
        path_by_url[decoded] = item["local_path"]

    link_pattern = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
    count = 0
    for relative in CONTENT_PATHS:
        source_path = ROOT / relative
        original = source_path.read_text(encoding="utf-8")

        def replace(match: re.Match) -> str:
            nonlocal count
            label, raw_target = match.group(1), match.group(2)
            if label.casefold() in {"source", "original source"}:
                return match.group(0)
            target = raw_target.strip("<>")
            parsed = urlparse(target)
            if parsed.netloc.casefold() not in {"mordheimer.net", "www.mordheimer.net"}:
                return match.group(0)
            base = urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip("/"), "", "", ""))
            local_target = path_by_url.get(base)
            if not local_target:
                decoded = urlunparse((parsed.scheme, parsed.netloc, unquote(parsed.path).rstrip("/"), "", "", ""))
                local_target = path_by_url.get(decoded)
            fallback_anchor = ""
            if not local_target and parsed.path.rstrip("/") == "/docs/campaigns/hired-swords/corefreelancer" and label.casefold() == "freelancer":
                local_target = "campaigns/hired-swords/core.md"
                fallback_anchor = "freelancer"
            if not local_target:
                return match.group(0)
            fragment_value = parsed.fragment or fallback_anchor
            fragment = f"#{fragment_value}" if fragment_value else ""
            count += 1
            return f"[{label}]({rel_link(relative, local_target, '')}{fragment})"

        updated = link_pattern.sub(replace, original)
        if updated != original:
            source_path.write_text(updated, encoding="utf-8")
    return count


def update_manifest_checksums() -> None:
    for item in MANIFEST["sources"]:
        path = ROOT / item["local_path"]
        if path.is_file():
            item["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    manifest_path = ROOT / "manifest.json"
    temp_path = manifest_path.with_suffix(".json.tmp")
    temp_path.write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temp_path, manifest_path)


def main() -> None:
    targets = make_target_map()
    total = 0
    changed = 0
    for relative in sorted(CONTENT_PATHS):
        path = ROOT / relative
        original = path.read_text(encoding="utf-8")
        lines = original.splitlines(keepends=True)
        output = []
        in_frontmatter = False
        saw_frontmatter = False
        in_code = False
        page_links = 0
        for line in lines:
            if line.strip() == "---" and not saw_frontmatter:
                in_frontmatter = not in_frontmatter
                if not in_frontmatter:
                    saw_frontmatter = True
                output.append(line)
                continue
            if in_frontmatter or line.lstrip().startswith("```"):
                if line.lstrip().startswith("```"):
                    in_code = not in_code
                output.append(line)
                continue
            if in_code or re.match(r"^\s*#{1,6}\s", line):
                output.append(line)
                continue
            linked, count = linkify_text(line, relative, targets)
            output.append(linked)
            page_links += count
        updated = "".join(output)
        total += page_links
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
        print(f"{relative}: +{page_links} links")
    localized = localize_in_scope_links()
    repaired = repair_local_anchors(targets)
    update_manifest_checksums()
    print(f"Added {total} cross-links across {changed} content files; localized {localized} archived links and repaired {repaired} fragments.")


if __name__ == "__main__":
    main()
