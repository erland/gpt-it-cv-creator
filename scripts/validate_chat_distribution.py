#!/usr/bin/env python3
import argparse, json, zipfile
from pathlib import Path

REQUIRED = {
    'START-HERE.md','VERSION','MANIFEST.json',
    'assistant/instructions.md','assistant/conversation-starters.md','assistant/runtime-contract.json',
    'assistant/policies/workflow-policy.md',
    'knowledge/artifact-delivery-contract.md','knowledge/cv-output-contract.md',
    'knowledge/cv-writing-guidelines.md','knowledge/job-fit-contract.md',
    'knowledge/research-evidence-contract.md','knowledge/source-research-guidelines.md',
}
FORBIDDEN_PREFIXES = ('evals/','.github/','docs/','workspace-template/','deliverables-template/','schemas/','templates/','build/','dist/')
FORBIDDEN_FILES = {'PROJECT.md','STATUS.md','project-status.yaml','gpt-project.yaml','tests-manifest.yaml'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--zip', required=True); ap.add_argument('--version', required=True)
    a=ap.parse_args(); zpath=Path(a.zip)
    if not zpath.exists(): raise SystemExit(f'Chat ZIP missing: {zpath}')
    with zipfile.ZipFile(zpath) as z:
        names=set(z.namelist())
        missing=sorted(REQUIRED-names)
        if missing: raise SystemExit('Missing required Chat files: '+', '.join(missing))
        bad=sorted(n for n in names if n in FORBIDDEN_FILES or n.startswith(FORBIDDEN_PREFIXES))
        if bad: raise SystemExit('Project-only files leaked into Chat ZIP: '+', '.join(bad[:20]))
        version=z.read('VERSION').decode().strip()
        if version != a.version: raise SystemExit(f'Version mismatch: {version} != {a.version}')
        manifest=json.loads(z.read('MANIFEST.json'))
        if manifest.get('adapter_id') != 'chatgpt_chat': raise SystemExit('Wrong adapter_id')
        start=z.read('START-HERE.md').decode()
        if 'håller normalt chatten kort' not in start: raise SystemExit('Compact-chat usage note missing')
    print(f'Chat distribution OK ({len(names)} files, version {a.version})')
if __name__=='__main__': main()
