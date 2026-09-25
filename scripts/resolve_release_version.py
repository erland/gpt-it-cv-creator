#!/usr/bin/env python3
from __future__ import annotations
import argparse,re,sys

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('tag'); args=ap.parse_args()
    tag=args.tag.strip()
    version=tag[1:] if tag.startswith('v') else tag
    if not re.fullmatch(r'\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?', version):
        print(f'Invalid release tag: {tag!r}. Expected 1.2.3 or v1.2.3.', file=sys.stderr)
        return 2
    print(version)
    return 0
if __name__=='__main__': raise SystemExit(main())
