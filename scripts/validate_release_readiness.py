#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path

def run(cmd):
    p=subprocess.run(cmd,text=True,capture_output=True)
    return p.returncode,(p.stdout+p.stderr).strip()

def gate(gates,name,cmd,blockers):
    rc,out=run(cmd)
    gates[name]={'status':'pass' if rc==0 else 'blocked','message':out[-1600:] if out else ('PASS' if rc==0 else 'FAILED')}
    if rc!=0: blockers.append(name)
    return rc

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--project-root',default='.'); ap.add_argument('--version',default='0.1.0-dev'); ap.add_argument('--out',default='reports/release-readiness.json'); args=ap.parse_args()
    root=Path(args.project_root).resolve(); py=sys.executable
    gates={}; blockers=[]; warnings=[]

    # Start from a clean source tree, then rebuild the candidate reproducibly.
    gate(gates,'hygiene_fix',[py,str(root/'scripts/project_hygiene.py'),'--project-root',str(root),'--mode','final','--fix'],blockers)
    gate(gates,'lint',[py,str(root/'scripts/lint_gpt_project.py'),'--project-root',str(root)],blockers)
    gate(gates,'model_robustness',[py,str(root/'scripts/validate_model_robustness.py'),'--project-root',str(root)],blockers)
    gate(gates,'eval_suite',[py,str(root/'scripts/validate_it_cv_evals.py'),'--project-root',str(root)],blockers)
    gate(gates,'build',[py,str(root/'scripts/build_distributions.py'),'--project-root',str(root),'--version',args.version],blockers)

    dist=root/'dist'; build=root/'build'
    chat=dist/f'it-cv-creator-chat-{args.version}.zip'; custom=dist/f'it-cv-creator-custom-gpt-{args.version}.zip'; project=dist/'it-cv-creator-project.zip'
    gate(gates,'chat_runtime',[py,str(root/'scripts/validate_chat_distribution.py'),'--zip',str(chat),'--version',args.version],blockers)
    gate(gates,'custom_runtime',[py,str(root/'scripts/validate_custom_gpt_distribution.py'),'--project-root',str(root),'--distribution-root',str(build/'custom-gpt')],blockers)
    gate(gates,'runtime_parity',[py,str(root/'scripts/validate_runtime_parity.py'),'--project-root',str(root),'--version',args.version,'--json-out','reports/runtime-parity.json','--md-out','reports/runtime-parity.md'],blockers)

    distributions={'project_zip':'ready' if project.exists() else 'blocked','chatgpt_chat':'ready' if chat.exists() else 'blocked','chatgpt_custom':'ready' if custom.exists() else 'blocked'}
    for k,v in distributions.items():
        if v=='blocked': blockers.append(k)
    result='ready' if not blockers and not warnings else ('ready_with_warnings' if not blockers else 'blocked')
    payload={'schema_version':1,'result':result,'gates':gates,'distributions':distributions,'warnings':warnings,'blockers':sorted(set(blockers))}
    outp=root/args.out; outp.parent.mkdir(parents=True,exist_ok=True); outp.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding='utf-8')
    print(json.dumps(payload,ensure_ascii=False,indent=2)); return 0 if result!='blocked' else 1
if __name__=='__main__': raise SystemExit(main())
