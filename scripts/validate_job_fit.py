#!/usr/bin/env python3
from __future__ import annotations
import argparse
import sys
from pathlib import Path
import yaml

STATUSES = {"supported", "partially_supported", "clarification_needed", "gap", "not_applicable"}
PRIORITIES = {"explicit_must", "explicit_merit", "implied_core", "contextual"}
ACTIONS = {"emphasize", "include", "compress", "omit", "ask_user"}
USABLE_STRENGTH = {"direct", "corroborated", "supported", "inferred"}


def fail(msg: str) -> None:
    print(f"ERROR: {msg}")
    raise SystemExit(1)


def load(path: Path) -> dict:
    if not path.exists():
        fail(f"file not found: {path}")
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("fit", nargs="?", default="workspace/fit-analysis.yaml")
    p.add_argument("ledger", nargs="?", default="workspace/research-ledger.yaml")
    args = p.parse_args()

    fit = load(Path(args.fit))
    ledger = load(Path(args.ledger))

    usable_claims = {}
    for c in ledger.get("claims") or []:
        if c.get("status") == "usable" and c.get("evidence_strength") in USABLE_STRENGTH:
            usable_claims[c.get("id")] = c

    req_ids = set()
    for req in fit.get("requirements") or []:
        rid = req.get("id")
        if not rid or rid in req_ids:
            fail("requirement IDs must be present and unique")
        req_ids.add(rid)
        if req.get("priority") not in PRIORITIES:
            fail(f"invalid priority for {rid}")
        match = req.get("match") or {}
        status = match.get("status")
        if status not in STATUSES:
            fail(f"invalid match status for {rid}")
        if match.get("cv_action") not in ACTIONS:
            fail(f"invalid cv_action for {rid}")
        claim_ids = list(match.get("claim_ids") or [])
        unknown_or_unusable = [cid for cid in claim_ids if cid not in usable_claims]
        if unknown_or_unusable:
            fail(f"{rid} references unknown or unusable claims: {', '.join(unknown_or_unusable)}")
        if status == "supported" and not claim_ids:
            fail(f"supported requirement {rid} must reference usable evidence")
        if status == "gap" and claim_ids:
            fail(f"gap requirement {rid} must not claim supporting evidence")
        if status == "clarification_needed" and match.get("cv_action") != "ask_user":
            fail(f"clarification_needed requirement {rid} must use cv_action=ask_user")
        if status in {"gap", "not_applicable"} and match.get("cv_action") == "emphasize":
            fail(f"{status} requirement {rid} cannot be emphasized")

    summary = fit.get("summary") or {}
    for key in ["clarification_requirement_ids", "strategy_focus_requirement_ids"]:
        unknown = set(summary.get(key) or []) - req_ids
        if unknown:
            fail(f"{key} references unknown requirements: {', '.join(sorted(unknown))}")

    print("PASS: job fit analysis is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
