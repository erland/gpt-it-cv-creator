#!/usr/bin/env python3
from __future__ import annotations
import argparse
import sys
from pathlib import Path
import yaml

IDENTITY = {"confirmed", "probable", "uncertain"}
SOURCE_CLASS = {"user_provided", "first_party", "official_third_party", "credible_secondary", "weak_secondary"}
APPROVAL = {"approved", "rejected", "pending", "identity_uncertain"}
STRENGTH = {"direct", "corroborated", "supported", "inferred", "uncertain"}
CLAIM_STATUS = {"usable", "clarification_required", "excluded"}
CONFLICT_STATUS = {"open", "resolved", "not_material"}


def fail(msg: str) -> None:
    print(f"ERROR: {msg}")
    raise SystemExit(1)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("ledger", nargs="?", default="workspace/research-ledger.yaml")
    args = p.parse_args()
    path = Path(args.ledger)
    if not path.exists():
        fail(f"ledger file not found: {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    sources = data.get("sources") or []
    claims = data.get("claims") or []
    conflicts = data.get("conflicts") or []

    src_ids = set()
    approved_ids = set()
    for s in sources:
        sid = s.get("id")
        if not sid or sid in src_ids:
            fail("source IDs must be present and unique")
        src_ids.add(sid)
        if s.get("identity_confidence") not in IDENTITY:
            fail(f"invalid identity_confidence for {sid}")
        if s.get("source_class") not in SOURCE_CLASS:
            fail(f"invalid source_class for {sid}")
        if s.get("approval_status") not in APPROVAL:
            fail(f"invalid approval_status for {sid}")
        if s.get("approval_status") == "approved":
            approved_ids.add(sid)

    claim_ids = set()
    for c in claims:
        cid = c.get("id")
        if not cid or cid in claim_ids:
            fail("claim IDs must be present and unique")
        claim_ids.add(cid)
        strength = c.get("evidence_strength")
        status = c.get("status")
        if strength not in STRENGTH:
            fail(f"invalid evidence_strength for {cid}")
        if status not in CLAIM_STATUS:
            fail(f"invalid claim status for {cid}")
        refs = set(c.get("source_ids") or [])
        unknown = refs - src_ids
        if unknown:
            fail(f"claim {cid} references unknown sources: {', '.join(sorted(unknown))}")
        unauthorized = refs - approved_ids
        if unauthorized:
            fail(f"claim {cid} references non-approved sources: {', '.join(sorted(unauthorized))}")
        if strength == "uncertain" and status == "usable":
            fail(f"uncertain claim {cid} cannot be usable")
        if strength == "inferred" and c.get("type") in {"employment", "certification", "education", "measurable_result"} and status == "usable":
            fail(f"inferred claim {cid} cannot create a hard CV fact")
        if c.get("type") == "measurable_result" and status == "usable" and strength not in {"direct", "corroborated"}:
            fail(f"measurable_result {cid} requires direct or corroborated evidence")

    for conf in conflicts:
        fid = conf.get("id")
        if conf.get("resolution_status") not in CONFLICT_STATUS:
            fail(f"invalid conflict status for {fid or '<missing>'}")
        unknown_claims = set(conf.get("claim_ids") or []) - claim_ids
        if unknown_claims:
            fail(f"conflict {fid} references unknown claims: {', '.join(sorted(unknown_claims))}")

    print("PASS: research ledger is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
