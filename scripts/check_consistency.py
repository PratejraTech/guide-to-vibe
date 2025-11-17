#!/usr/bin/env python
"""
Consistency check script for Vibe/Cursor/OpenCode repo.

Run this BEFORE building:
    python scripts/check_consistency.py

Responsibilities:
- Ensure required governance files exist.
- Ensure .agents/folders.mdc exists and is parseable.
- Ensure top-level folder structure matches folders.mdc.
- Ensure module MDC files reference folders.mdc (no redefined structure).
"""

from __future__ import annotations

import sys
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None


# Adjust if you place the script elsewhere
ROOT = Path(__file__).resolve().parents[1]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def error(msg: str) -> str:
    return f"[ERROR] {msg}"


def warn(msg: str) -> str:
    return f"[WARN]  {msg}"


def info(msg: str) -> str:
    return f"[INFO]  {msg}"


def load_text(path: Path) -> Optional[str]:
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def extract_front_matter(content: str) -> Tuple[Dict, str]:
    """
    Extract YAML front matter from an .mdc-style file.
    Returns (front_matter_dict, body).
    If no front matter, returns ({}, full_content).
    """
    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)
    # parts: ["", "<yaml>\n", "<body>"]
    if len(parts) < 3:
        return {}, content

    yaml_block = parts[1].strip()
    body = parts[2].lstrip("\n")

    if yaml is None:
        # YAML parsing not available, just return raw block as a hint.
        return {"_raw_yaml": yaml_block}, body

    try:
        fm = yaml.safe_load(yaml_block) or {}
        if not isinstance(fm, dict):
            fm = {}
        return fm, body
    except Exception:
        # YAML parse error – caller should treat as error condition
        return {"_yaml_error": yaml_block}, body


def extract_first_code_block(content: str) -> Optional[str]:
    """
    Extract the first fenced code block (``` ... ```).
    Returns the inner text or None.
    """
    fence_pattern = re.compile(r"```(?:[a-zA-Z0-9_-]*)\s*([\s\S]*?)```", re.MULTILINE)
    match = fence_pattern.search(content)
    if not match:
        return None
    return match.group(1)


def parse_expected_top_level_dirs_from_folders_mdc(content: str) -> List[str]:
    """
    Parse folders.mdc to infer expected top-level directories.
    We assume the first code block shows a tree like:

        PROJECT_NAME/
          .agents/
          backend/
          frontend/
          ...

    We then extract `.agents`, `backend`, `frontend`, etc., ignoring the root name.
    """
    block = extract_first_code_block(content)
    if block is None:
        return []

    expected: List[str] = []
    for raw_line in block.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        # Example lines:
        # "PROJECT_NAME/"
        # "  backend/"
        # "  docs/"
        if line.endswith("/"):
            # Strip trailing slash and possible root prefix
            item = line.rstrip("/")
            # Drop leading tree markers or indent
            item = item.lstrip("|- ").strip()
            # Only take the first path component
            parts = item.split("/", 1)
            name = parts[0]
            if name == "" or name.upper() == "PROJECT_NAME":
                continue
            if name not in expected:
                expected.append(name)
    return expected


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_required_files() -> List[str]:
    errors: List[str] = []
    warnings: List[str] = []

    required_files = [
        ROOT / ".cursorrules",
        ROOT / ".agents" / "folders.mdc",
        ROOT / ".agents" / "AGENTS.md",
        ROOT / ".agents" / "backend.mdc",
        ROOT / ".agents" / "frontend.mdc",
        ROOT / ".agents" / "integration.mdc",
    ]

    for path in required_files:
        if not path.exists():
            errors.append(error(f"Missing required file: {path.relative_to(ROOT)}"))

    return errors + warnings


def check_folders_mdc_structure() -> List[str]:
    errors: List[str] = []
    warnings: List[str] = []

    folders_path = ROOT / ".agents" / "folders.mdc"
    content = load_text(folders_path)
    if content is None:
        errors.append(error("Cannot read .agents/folders.mdc"))
        return errors

    front_matter, body = extract_front_matter(content)
    if "_yaml_error" in front_matter:
        errors.append(error("YAML front matter in .agents/folders.mdc is invalid"))
    elif not front_matter:
        warnings.append(warn("No YAML front matter found in .agents/folders.mdc"))

    expected_dirs = parse_expected_top_level_dirs_from_folders_mdc(body)
    if not expected_dirs:
        warnings.append(warn("Could not infer expected top-level dirs from folders.mdc (empty or malformed code block)."))
        return errors + warnings

    # Compare with filesystem
    top_level_dirs_on_disk = sorted(
        [p.name for p in ROOT.iterdir() if p.is_dir()]
    )

    # Allow some extra dirs that are commonly present
    allowed_extra = {".git", ".idea", ".vscode", "__pycache__"}

    # Check that all expected dirs exist on disk
    for d in expected_dirs:
        if d not in top_level_dirs_on_disk:
            errors.append(error(f"Expected top-level directory '{d}' from folders.mdc is missing on disk."))

    # Optionally warn about unexpected dirs
    for d in top_level_dirs_on_disk:
        if d in allowed_extra:
            continue
        if d not in expected_dirs and d != ".agents":
            warnings.append(warn(
                f"Top-level directory '{d}' exists on disk but is not listed in folders.mdc. "
                "Confirm this is intentional."
            ))

    return errors + warnings


def check_module_mdc_structure_reference() -> List[str]:
    """
    Ensure backend/frontend/integration MDC files:
    - have YAML front matter
    - set `structure: refer-to-folders.mdc`
    - have correct `module` field
    """
    errors: List[str] = []
    warnings: List[str] = []

    expected_modules = {
        "backend.mdc": "backend",
        "frontend.mdc": "frontend",
        "integration.mdc": "integration",
    }

    for filename, expected_module in expected_modules.items():
        path = ROOT / ".agents" / filename
        content = load_text(path)
        if content is None:
            errors.append(error(f"Missing MDC file: .agents/{filename}"))
            continue

        fm, body = extract_front_matter(content)
        if not fm:
            errors.append(error(f".agents/{filename} is missing YAML front matter."))
            continue

        module_value = fm.get("module")
        if module_value != expected_module:
            errors.append(error(
                f".agents/{filename}: front matter 'module' should be '{expected_module}', found '{module_value}'."
            ))

        structure = fm.get("structure")
        if structure != "refer-to-folders.mdc":
            errors.append(error(
                f".agents/{filename}: front matter 'structure' should be 'refer-to-folders.mdc' "
                f"to delegate structure to folders.mdc (found '{structure}')."
            ))

    return errors + warnings


def check_playbook_presence() -> List[str]:
    """
    Soft check for playbook prompt presence. This is non-fatal but useful.
    You can adapt the paths to your actual layout.
    """
    errors: List[str] = []
    warnings: List[str] = []

    # Two common layouts:
    # - Root files: "01 - Draft Plan.md", ...
    # - docs/playbooks: "01-draft-plan.md", ...
    root_candidates = [
        "01 - Draft Plan.md",
        "02 - Folder Structure.md",
        "03 - Product Requirements Document.md",
        "04 - Architecture Document.md",
        "05 - Backend Plan.md",
        "06 - Frontend Plan.md",
        "07 - Integration.md",
    ]

    docs_candidates = [
        "01-draft-plan.md",
        "02-folder-structure.md",
        "03-prd.md",
        "04-architecture.md",
        "05-backend-plan.md",
        "06-frontend-plan.md",
        "07-integration.md",
    ]

    root_ok = all((ROOT / name).exists() for name in root_candidates)
    docs_ok = all((ROOT / "docs" / "playbooks" / name).exists() for name in docs_candidates)

    if not root_ok and not docs_ok:
        warnings.append(warn(
            "Playbook prompt files (01–07) not found in root or docs/playbooks/. "
            "Ensure they exist somewhere documented, or update this script."
        ))

    return errors + warnings


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    all_messages: List[str] = []

    all_messages.extend(check_required_files())
    all_messages.extend(check_folders_mdc_structure())
    all_messages.extend(check_module_mdc_structure_reference())
    all_messages.extend(check_playbook_presence())

    errors = [m for m in all_messages if m.startswith("[ERROR]")]
    warnings = [m for m in all_messages if m.startswith("[WARN]")]

    if warnings:
        print(info("Consistency check completed with warnings:"))
        for w in warnings:
            print(w)
        print()

    if errors:
        print(info("Consistency check FAILED:"))
        for e in errors:
            print(e)
        print()
        print("Build should NOT proceed until these issues are resolved.")
        return 1

    print(info("Consistency check PASSED. Repository is structurally consistent."))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())