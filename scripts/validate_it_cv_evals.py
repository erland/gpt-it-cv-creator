#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys
import yaml

REQUIRED_SCENARIOS = {
    "wrong-person-search-result",
    "rejected-source",
    "conflicting-evidence",
    "target-role-without-job-ad",
    "job-ad-is-not-candidate-evidence",
    "resume-workspace-state",
    "late-user-material",
    "terminal-after-delivery",
    "compact-chat",
    "new-source-after-approval",
    "cv-length-choice",
}

REQUIRED_CANONICAL_MARKERS = {
    "SOURCE-APPROVAL-GATE",
    "NO-FABRICATION",
    "EVIDENCE-TRACEABILITY",
    "TARGET-FIRST",
    "USER-CONTROL",
    "COMPACT-CHAT",
}


def fail(msg: str) -> None:
    raise ValueError(msg)


def get_prompt(case: dict) -> str:
    if isinstance(case.get("prompt"), str):
        return case["prompt"].strip()
    inp = case.get("input") or {}
    if isinstance(inp, dict) and isinstance(inp.get("prompt"), str):
        return inp["prompt"].strip()
    return ""


def validate_case(path: Path) -> str:
    try:
        case = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        fail(f"EVAL-001: invalid YAML in {path.name}: {exc}")
    if not isinstance(case, dict):
        fail(f"EVAL-002: {path.name} must contain a mapping")
    cid = case.get("id")
    if not isinstance(cid, str) or not cid.strip():
        fail(f"EVAL-003: {path.name} is missing id")
    if not get_prompt(case):
        fail(f"EVAL-004: {cid} is missing a concrete prompt")
    expected = case.get("expected")
    if not isinstance(expected, dict) or not expected:
        fail(f"EVAL-005: {cid} is missing expected behavior")
    meaningful = any(k in expected for k in ("behavior", "must_include", "must_not_do", "must_not_include", "must_preserve_core_contract"))
    if not meaningful:
        fail(f"EVAL-006: {cid} expected block is too vague")
    return cid


def validate(root: Path) -> None:
    scenario_dir = root / "evals" / "model-compatibility"
    if not scenario_dir.is_dir():
        fail("EVAL-010: model-compatibility suite is missing")

    ids: list[str] = []
    for path in sorted(scenario_dir.glob("*.yaml")):
        ids.append(validate_case(path))
    if len(ids) != len(set(ids)):
        fail("EVAL-011: duplicate eval IDs")

    missing = sorted(REQUIRED_SCENARIOS - set(ids))
    if missing:
        fail("EVAL-012: missing required CV scenarios: " + ", ".join(missing))

    canonical = (root / "assistant" / "instructions.md").read_text(encoding="utf-8")
    missing_markers = sorted(marker for marker in REQUIRED_CANONICAL_MARKERS if marker not in canonical)
    if missing_markers:
        fail("EVAL-013: canonical instruction lost core markers: " + ", ".join(missing_markers))

    # Step-7-specific regression hooks. These phrases make the intended state behavior
    # explicit enough to survive compilation to smaller runtimes.
    required_phrases = [
        "material som användaren själv tillhandahåller",
        "när fasen är `completed`",
        "fel identitet/avvisad",
        "Rekommendera åt mig",
        "Researchunderlaget förblir komplett",
    ]
    for phrase in required_phrases:
        if phrase not in canonical:
            fail(f"EVAL-014: canonical instruction is missing step-7 regression rule: {phrase}")

    print(f"IT CV eval suite OK ({len(ids)} scenarios)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    args = parser.parse_args()
    try:
        validate(Path(args.project_root).resolve())
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
