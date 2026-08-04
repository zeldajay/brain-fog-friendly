#!/usr/bin/env python3
"""Configure Brain Fog Friendly in Codex's global AGENTS.md."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import stat
import sys
import tempfile


BEGIN_MARKER = "<!-- brain-fog-friendly:start -->"
END_MARKER = "<!-- brain-fog-friendly:end -->"

LANGUAGES = (
    ("en", "English"),
    ("zh-cn", "简体中文"),
    ("ja", "日本語"),
    ("ru", "Русский"),
    ("ar", "العربية"),
    ("ko", "한국어"),
    ("es", "Español"),
    ("fr", "Français"),
    ("de", "Deutsch"),
    ("pt-br", "Português do Brasil"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Choose a Brain Fog Friendly language or disable it globally."
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument(
        "--language",
        choices=tuple(code for code, _ in LANGUAGES),
        help="Language code to enable.",
    )
    action.add_argument(
        "--disable",
        action="store_true",
        help="Remove Brain Fog Friendly from the global AGENTS.md.",
    )
    parser.add_argument(
        "--agents-file",
        type=Path,
        help=argparse.SUPPRESS,
    )
    return parser.parse_args()


def global_agents_path() -> Path:
    configured_root = os.environ.get("CODEX_HOME")
    codex_root = Path(configured_root).expanduser() if configured_root else Path.home() / ".codex"
    return codex_root / "AGENTS.md"


def instruction_body(source_path: Path) -> str:
    contents = source_path.read_text(encoding="utf-8")
    if not contents.startswith("---\n"):
        return contents.strip()

    frontmatter_end = contents.find("\n---\n", 4)
    if frontmatter_end == -1:
        raise RuntimeError(f"Invalid frontmatter in {source_path.name}")
    return contents[frontmatter_end + len("\n---\n") :].strip()


def managed_block(language_code: str, language_label: str, body: str) -> str:
    return (
        f"{BEGIN_MARKER}\n"
        f"\n## Brain Fog Friendly ({language_label}, {language_code})\n"
        f"\n{body}\n"
        f"\n{END_MARKER}\n"
    )


def find_managed_block(contents: str) -> tuple[int, int] | None:
    begin_count = contents.count(BEGIN_MARKER)
    end_count = contents.count(END_MARKER)
    if begin_count == 0 and end_count == 0:
        return None
    if begin_count != 1 or end_count != 1:
        raise RuntimeError(
            "Global AGENTS.md contains malformed or duplicate brain-fog-friendly markers."
        )

    begin = contents.index(BEGIN_MARKER)
    end = contents.index(END_MARKER) + len(END_MARKER)
    if end <= begin:
        raise RuntimeError("Global AGENTS.md contains reversed brain-fog-friendly markers.")
    if contents[end : end + 1] == "\n":
        end += 1
    return begin, end


def enable(contents: str, block: str) -> str:
    location = find_managed_block(contents)
    if location is not None:
        begin, end = location
        return contents[:begin] + block + contents[end:]

    if not contents:
        return block
    separator = "\n" if contents.endswith("\n") else "\n\n"
    return contents + separator + block


def disable(contents: str) -> tuple[str, bool]:
    location = find_managed_block(contents)
    if location is None:
        return contents, False

    begin, end = location
    before = contents[:begin]
    after = contents[end:]
    if before.endswith("\n\n"):
        before = before[:-1]
    return before + after, True


def atomic_write(path: Path, contents: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing_mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else None
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            delete=False,
        ) as temporary_file:
            temporary_file.write(contents)
            temporary_path = Path(temporary_file.name)
        os.replace(temporary_path, path)
        if existing_mode is not None:
            path.chmod(existing_mode)
    except Exception:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
        raise


def main() -> int:
    args = parse_args()
    agents_path = args.agents_file.expanduser() if args.agents_file else global_agents_path()
    current_contents = agents_path.read_text(encoding="utf-8") if agents_path.exists() else ""

    if args.disable:
        updated_contents, changed = disable(current_contents)
        if not changed:
            print(f"\nBrain Fog Friendly is already disabled in {agents_path}")
            return 0
        atomic_write(agents_path, updated_contents)
        print(f"\nDisabled Brain Fog Friendly in {agents_path}")
        return 0

    language_code = args.language
    language_label = dict(LANGUAGES)[language_code]
    plugin_root = Path(__file__).resolve().parents[3]
    source_path = plugin_root / f"brain-fog-friendly-{language_code}.md"
    if not source_path.is_file():
        raise RuntimeError(f"Missing language file: {source_path}")

    body = instruction_body(source_path)
    block = managed_block(language_code, language_label, body)
    atomic_write(agents_path, enable(current_contents, block))
    print(f"\nEnabled {language_label} in {agents_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1)
