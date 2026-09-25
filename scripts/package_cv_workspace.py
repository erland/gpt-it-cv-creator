#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
import zipfile
from pathlib import Path

ALLOWED_ROOTS = ("workspace", "deliverables")
EXCLUDED_PARTS = {"__pycache__", ".git", "dist", "build", ".DS_Store"}
EXCLUDED_SUFFIXES = {".pyc", ".log", ".tmp"}


def include(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    if not rel.parts or rel.parts[0] not in ALLOWED_ROOTS:
        return False
    if any(part in EXCLUDED_PARTS for part in rel.parts):
        return False
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return False
    if any(x in path.name.lower() for x in ("secret", "token", "password", ".env")):
        return False
    return path.is_file()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project-root", default=".")
    ap.add_argument("--output", default="deliverables/research-workspace.zip")
    args = ap.parse_args()
    root = Path(args.project_root).resolve()
    out = (root / args.output).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    files = sorted(p for base in ALLOWED_ROOTS if (root/base).exists() for p in (root/base).rglob("*") if include(p, root) and p.resolve() != out)
    if not files:
        raise SystemExit("ERROR: no workspace/deliverable files to package")
    manifest_lines = ["schema_version: 1", "files:"]
    for p in files:
        rel = p.relative_to(root).as_posix()
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        manifest_lines.append(f"  - path: {rel}")
        manifest_lines.append(f"    sha256: {digest}")
    readme = """# IT CV Creator research workspace\n\nDetta paket innehåller strukturerat arbetsunderlag och leverabler. Externa webbsidor lagras normalt inte i fulltext; se källreferenser och evidence metadata i workspace.\n\nVid återupptagning: börja med workspace/workflow-state.yaml.\n"""
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for p in files:
            z.write(p, p.relative_to(root).as_posix())
        z.writestr("manifest.yaml", "\n".join(manifest_lines) + "\n")
        z.writestr("README.md", readme)
    print(f"PASS: packaged {len(files)} files -> {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
