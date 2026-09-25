#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
try:
    import yaml
except Exception as exc:
    raise SystemExit('PyYAML is required') from exc

REQUIRED = {
    'README.md','COMPATIBILITY.md','VERSION','MANIFEST.json',
    'builder/instructions.md','builder/conversation-starters.md','builder/capabilities.md',
    'builder/runtime-contract.json','builder/compilation-report.json'
}
FORBIDDEN_PREFIXES = ('evals/','.github/','schemas/','templates/','workspace-template/','deliverables-template/','scripts/')


def fail(msg: str) -> None:
    print(f'FAIL: {msg}')
    raise SystemExit(1)


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--project-root', default='.')
    ap.add_argument('--distribution-root')
    args=ap.parse_args()
    root=Path(args.project_root).resolve()
    cfg=yaml.safe_load((root/'gpt-project.yaml').read_text(encoding='utf-8'))
    dist=Path(args.distribution_root).resolve() if args.distribution_root else root/'build'/'custom-gpt'
    if not dist.exists(): fail(f'distribution root missing: {dist}')
    files={p.relative_to(dist).as_posix() for p in dist.rglob('*') if p.is_file()}
    missing=sorted(REQUIRED-files)
    if missing: fail('missing required files: '+', '.join(missing))
    bad=sorted(f for f in files if f.startswith(FORBIDDEN_PREFIXES) or f in {'PROJECT.md','STATUS.md','project-status.yaml','gpt-project.yaml','tests-manifest.yaml'})
    if bad: fail('project-only files leaked into Custom GPT package: '+', '.join(bad))

    instruction=(dist/'builder/instructions.md').read_text(encoding='utf-8')
    max_chars=int(cfg['runtime']['custom_gpt']['instruction']['max_characters'])
    if len(instruction)>max_chars: fail(f'instructions {len(instruction)} > {max_chars} characters')
    markers=cfg.get('instructions',{}).get('core_contract',{}).get('required_markers',[])
    absent=[m for m in markers if m not in instruction]
    if absent: fail('missing core markers: '+', '.join(absent))

    starters=(dist/'builder/conversation-starters.md').read_text(encoding='utf-8').strip()
    if not starters: fail('conversation starters are empty')
    cap=(dist/'builder/capabilities.md').read_text(encoding='utf-8')
    for term in ('Webbsökning','Filhantering'):
        if term not in cap: fail(f'capabilities missing {term}')

    kp=dist/'builder/knowledge-package'
    knowledge=[p for p in kp.rglob('*') if p.is_file()] if kp.exists() else []
    max_files=int(cfg['runtime']['custom_gpt']['knowledge']['max_files'])
    if not knowledge: fail('knowledge package is empty')
    if len(knowledge)>max_files: fail(f'knowledge files {len(knowledge)} > {max_files}')

    report=json.loads((dist/'builder/compilation-report.json').read_text(encoding='utf-8'))
    if report.get('instruction',{}).get('compiled_characters') != len(instruction):
        fail('compilation report instruction length differs from actual file')
    if report.get('knowledge',{}).get('selected_files') != len(knowledge):
        fail('compilation report knowledge count differs from actual package')
    if report.get('knowledge',{}).get('excluded'):
        fail('canonical knowledge unexpectedly excluded for this project')

    contract=json.loads((dist/'builder/runtime-contract.json').read_text(encoding='utf-8'))
    if contract.get('runtime_id')!='chatgpt_custom': fail('runtime contract id is not chatgpt_custom')
    if contract.get('adapter',{}).get('builder_package') is not True: fail('runtime contract missing builder_package=true')

    manifest=json.loads((dist/'MANIFEST.json').read_text(encoding='utf-8'))
    if manifest.get('adapter_id')!='chatgpt_custom': fail('manifest adapter_id mismatch')
    version=(dist/'VERSION').read_text(encoding='utf-8').strip()
    if manifest.get('version')!=version: fail('manifest/version mismatch')

    print(f'PASS: Custom GPT distribution validated ({len(instruction)} chars, {len(knowledge)} Knowledge files, {len(files)} files total)')

if __name__=='__main__': main()
