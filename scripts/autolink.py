#!/usr/bin/env python3
"""Auto-link script for CampaignWiki.

Discovers entity titles across all docs/ markdown files and replaces
unlinked mentions with proper Docusaurus relative-path links.

Usage:
    python scripts/autolink.py           # dry-run: prints proposed changes
    python scripts/autolink.py --apply   # writes changes to disk
"""

import difflib
import os
import re
import sys
from pathlib import Path

DOCS_DIR = Path(__file__).parent.parent / "docs"


def parse_frontmatter(content: str) -> tuple[dict, str, str]:
    """Parse YAML frontmatter. Returns (fields, frontmatter_block, body).

    frontmatter_block includes the opening and closing --- delimiters.
    The body is everything after the closing --- line.
    """
    if not content.startswith("---"):
        return {}, "", content

    rest = content[3:]  # strip opening ---
    end_idx = rest.find("\n---")
    if end_idx == -1:
        return {}, "", content

    fm_raw = rest[:end_idx]
    body = rest[end_idx + 4:]  # skip \n---
    frontmatter_block = "---" + fm_raw + "\n---"

    fields: dict[str, str] = {}
    for line in fm_raw.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()

    return fields, frontmatter_block, body


def collect_titles(docs_dir: Path) -> dict[str, Path]:
    """Walk docs_dir and return {title: file_path} for all titled pages."""
    title_map: dict[str, Path] = {}
    for md_file in sorted(docs_dir.rglob("*.md")):
        try:
            content = md_file.read_text(encoding="utf-8")
        except OSError:
            continue
        fields, _, _ = parse_frontmatter(content)
        title = fields.get("title", "").strip()
        if title:
            title_map[title] = md_file
    return title_map


# Matches any existing Markdown link so we can skip those segments.
_LINK_RE = re.compile(r"(\[.*?\]\(.*?\))", re.DOTALL)


def linkify_body(body: str, source_file: Path, title_map: dict[str, Path]) -> str:
    """Replace unlinked title mentions in body text with markdown links.

    Longer titles are processed first to avoid partial matches.
    Already-linked text (inside [...](…)) is not double-wrapped — we split
    the body on existing links and only substitute in the non-link segments.
    Self-references are skipped.
    """
    sorted_titles = sorted(title_map.keys(), key=len, reverse=True)

    for title in sorted_titles:
        target_file = title_map[title]
        if target_file.resolve() == source_file.resolve():
            continue

        rel_path = os.path.relpath(target_file, source_file.parent)
        rel_path_str = rel_path.replace(os.sep, "/")

        pattern = re.compile(r"\b" + re.escape(title) + r"\b", re.IGNORECASE)
        replacement = f"[{title}]({rel_path_str})"

        # Split on existing links; odd-indexed parts are the links themselves.
        # Only substitute in the even-indexed (non-link) parts.
        parts = _LINK_RE.split(body)
        for i in range(0, len(parts), 2):  # even indices = non-link text
            parts[i] = pattern.sub(replacement, parts[i])
        body = "".join(parts)

    return body


def process_file(
    md_file: Path,
    title_map: dict[str, Path],
    apply: bool = False,
) -> bool:
    """Process a single markdown file.

    Returns True if the file was (or would be) changed.
    In dry-run mode, prints a unified diff to stdout.
    In apply mode, writes the updated content to disk.
    """
    content = md_file.read_text(encoding="utf-8")
    _, fm_block, body = parse_frontmatter(content)

    new_body = linkify_body(body, md_file, title_map)

    if new_body == body:
        return False

    new_content = fm_block + new_body

    if apply:
        md_file.write_text(new_content, encoding="utf-8")
        print(f"Updated: {md_file}", file=sys.stderr)
    else:
        old_lines = content.splitlines(keepends=True)
        new_lines = new_content.splitlines(keepends=True)
        diff = difflib.unified_diff(
            old_lines,
            new_lines,
            fromfile=str(md_file),
            tofile=str(md_file),
        )
        sys.stdout.writelines(diff)

    return True


def main() -> None:
    apply = "--apply" in sys.argv

    title_map = collect_titles(DOCS_DIR)
    print(f"Discovered {len(title_map)} titled pages.", file=sys.stderr)

    changed = 0
    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        if process_file(md_file, title_map, apply=apply):
            changed += 1

    action = "Updated" if apply else "Would update"
    print(f"{action} {changed} file(s).", file=sys.stderr)


if __name__ == "__main__":
    main()
