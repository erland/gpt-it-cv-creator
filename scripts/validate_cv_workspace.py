#!/usr/bin/env python3
from __future__ import annotations
import argparse
import sys
from pathlib import Path
import yaml

PHASES = [
    "intake", "source_discovery", "source_approval", "deep_research",
    "target_analysis", "clarification", "cv_strategy", "drafting",
    "finalization", "completed"
]

def fail(msg: str) -> None:
    print(f"ERROR: {msg}")
    raise SystemExit(1)

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("state", nargs="?", default="workspace/workflow-state.yaml")
    args = p.parse_args()
    path = Path(args.state)
    if not path.exists():
        fail(f"state file not found: {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    workflow = data.get("workflow", {})
    gate = data.get("source_gate", {})
    research = data.get("research", {})
    cv_length = data.get("cv_length", {})
    phase = workflow.get("current_phase")
    if phase not in PHASES:
        fail(f"unknown current_phase: {phase!r}")

    requested_length = cv_length.get("requested", "short")
    resolved_length = cv_length.get("resolved")
    if requested_length not in {"short", "extended", "recommended"}:
        fail(f"invalid cv_length.requested: {requested_length!r}")
    if resolved_length not in {None, "short", "extended"}:
        fail(f"invalid cv_length.resolved: {resolved_length!r}")
    if requested_length in {"short", "extended"} and resolved_length not in {None, requested_length}:
        fail("resolved CV length conflicts with explicit user choice")
    if phase in PHASES[PHASES.index("drafting"):]:
        if requested_length == "recommended" and resolved_length not in {"short", "extended"}:
            fail("recommended CV length must be resolved before drafting")
        if requested_length in {"short", "extended"} and resolved_length is None:
            # Explicit choices may be treated as self-resolving, but persist them before drafting.
            fail("explicit CV length must be persisted as resolved before drafting")

    approved = list(gate.get("approved_source_ids") or [])
    rejected = list(gate.get("rejected_source_ids") or [])
    pending = list(gate.get("pending_source_ids") or [])
    analyzed = list(research.get("analyzed_source_ids") or [])
    if set(approved) & set(rejected):
        fail("a source cannot be both approved and rejected")
    if set(approved) & set(pending):
        fail("a source cannot be both approved and pending")
    if gate.get("approval_complete") and pending:
        fail("approval_complete cannot be true while pending sources remain")
    if phase in PHASES[PHASES.index("deep_research"):]:
        if not gate.get("approval_requested"):
            fail("cannot enter deep_research or later before approval was requested")
        if not gate.get("approval_complete"):
            fail("cannot enter deep_research or later before source approval is complete")
    if research.get("deep_research_started") and not gate.get("approval_complete"):
        fail("deep_research_started requires approval_complete=true")
    unauthorized = sorted(set(analyzed) - set(approved))
    if unauthorized:
        fail("analyzed sources are not approved: " + ", ".join(unauthorized))
    print("PASS: CV workspace state is valid")
    return 0

if __name__ == "__main__":
    sys.exit(main())
