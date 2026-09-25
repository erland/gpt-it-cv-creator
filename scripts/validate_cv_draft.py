#!/usr/bin/env python3
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

REQUIRED_GROUPS = {
    "cover_letter": [r"^##\s+Personligt brev\b", r"^##\s+Cover letter\b"],
    "profile": [r"^##\s+Professionell profil\b", r"^##\s+Professional profile\b", r"^##\s+Profile\b"],
    "skills": [r"^##\s+Nyckelkompetenser\b", r"^##\s+Key skills\b", r"^##\s+Core competencies\b"],
    "experience": [r"^##\s+Arbetslivserfarenhet\b", r"^##\s+Work experience\b", r"^##\s+Experience\b"],
    "education": [r"^##\s+Utbildning och certifieringar\b", r"^##\s+Education(?: and certifications)?\b"],
}

PLACEHOLDER_RE = re.compile(r"\{\{[^}]+\}\}")


def fail(msg: str) -> None:
    print(f"ERROR: {msg}")
    raise SystemExit(1)


def has_heading(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, flags=re.MULTILINE | re.IGNORECASE) for pattern in patterns)


def section_text(text: str, heading_pattern: str) -> str:
    m = re.search(heading_pattern, text, flags=re.MULTILINE | re.IGNORECASE)
    if not m:
        return ""
    start = m.end()
    nxt = re.search(r"^##\s+", text[start:], flags=re.MULTILINE)
    end = start + nxt.start() if nxt else len(text)
    return text[start:end].strip()


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\wÅÄÖåäö'-]+\b", text, flags=re.UNICODE))


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("draft", nargs="?", default="deliverables/cv-draft.md")
    p.add_argument("--allow-placeholders", action="store_true")
    p.add_argument("--length-profile", choices=["short", "extended"], default="short")
    args = p.parse_args()

    path = Path(args.draft)
    if not path.exists():
        fail(f"file not found: {path}")
    text = path.read_text(encoding="utf-8")

    for name, patterns in REQUIRED_GROUPS.items():
        if not has_heading(text, patterns):
            fail(f"missing required section: {name}")

    if not args.allow_placeholders and PLACEHOLDER_RE.search(text):
        fail("draft contains unresolved placeholders")

    cover = ""
    for pattern in REQUIRED_GROUPS["cover_letter"]:
        cover = section_text(text, pattern)
        if cover:
            break
    cover_words = word_count(cover)
    if not args.allow_placeholders and cover_words and not 120 <= cover_words <= 500:
        fail(f"cover letter length outside expected compact range: {cover_words} words")

    total_words = word_count(text)
    max_words = 2400 if args.length_profile == "short" else 4200
    page_target = "2–4" if args.length_profile == "short" else "4–7"
    if not args.allow_placeholders and total_words > max_words:
        fail(f"draft is too long for {args.length_profile} ({page_target} page target): {total_words} words")

    banned = [
        r"\bskill level\s*[:=]?\s*\d+%",
        r"\bkompetensnivå\s*[:=]?\s*\d+%",
        r"[★☆]{3,}",
    ]
    if any(re.search(pat, text, flags=re.IGNORECASE) for pat in banned):
        fail("draft contains prohibited pseudo-precision for skill level")

    print(f"PASS: CV draft structure is valid for {args.length_profile} ({total_words} words; cover letter {cover_words} words)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
