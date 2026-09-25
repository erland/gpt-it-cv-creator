#!/usr/bin/env python3
from __future__ import annotations
import argparse
import sys
from pathlib import Path
import yaml

ALLOWED = {"docx", "pdf", "markdown"}

def fail(msg: str) -> None:
    print(f"ERROR: {msg}")
    raise SystemExit(1)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest", nargs="?", default="deliverables/delivery-manifest.yaml")
    ap.add_argument("--project-root", default=".")
    args = ap.parse_args()
    root = Path(args.project_root).resolve()
    path = Path(args.manifest)
    if not path.is_absolute(): path = root / path
    if not path.exists(): fail(f"manifest not found: {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if data.get("schema_version") != 1: fail("unsupported schema_version")
    source = data.get("source_markdown")
    if not source or not (root/source).exists(): fail("source_markdown does not exist")
    requested = set(data.get("requested_formats") or [])
    if not requested <= ALLOWED: fail("unknown requested format")
    created = data.get("created_artifacts") or []
    created_formats = set()
    for item in created:
        fmt, rel = item.get("format"), item.get("path")
        if not fmt or not rel: fail("created artifact missing format/path")
        if not (root/rel).exists(): fail(f"claimed artifact does not exist: {rel}")
        created_formats.add(fmt)
    missing = requested - created_formats
    if missing and not data.get("limitations"):
        fail("requested formats missing without documented limitation: " + ", ".join(sorted(missing)))
    print("PASS: delivery manifest is consistent with files on disk")
    return 0

if __name__ == "__main__":
    sys.exit(main())
