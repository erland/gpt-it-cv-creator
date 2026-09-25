#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, zipfile
from pathlib import Path

MARKERS = [
    "SOURCE-APPROVAL-GATE","NO-FABRICATION","EVIDENCE-TRACEABILITY",
    "TARGET-FIRST","USER-CONTROL","COMPACT-CHAT"
]
REQUIREMENTS = [
    ("behavior","source_gate","Source approval before deep research","critical","SOURCE-APPROVAL-GATE"),
    ("behavior","no_fabrication","No fabricated qualifications","critical","NO-FABRICATION"),
    ("behavior","traceability","Evidence traceability","critical","EVIDENCE-TRACEABILITY"),
    ("behavior","target_first","Target role required","important","TARGET-FIRST"),
    ("behavior","user_control","User controls external sources","critical","USER-CONTROL"),
    ("behavior","compact_chat","Compact chat behavior","important","COMPACT-CHAT"),
]

def read_zip_text(zp: Path, preferred: list[str]) -> str:
    with zipfile.ZipFile(zp) as zf:
        names = set(zf.namelist())
        for name in preferred:
            if name in names:
                return zf.read(name).decode("utf-8", errors="replace")
    return ""

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--project-root", default=".")
    ap.add_argument("--version", default="0.1.0-dev")
    ap.add_argument("--json-out")
    ap.add_argument("--md-out")
    args=ap.parse_args()
    root=Path(args.project_root).resolve()
    dist=root/"dist"
    chat=dist/f"it-cv-creator-chat-{args.version}.zip"
    custom=dist/f"it-cv-creator-custom-gpt-{args.version}.zip"
    if not chat.exists() or not custom.exists():
        raise SystemExit("Build both runtime ZIPs before parity validation")

    chat_text=read_zip_text(chat,["assistant/instructions.md"])
    custom_text=read_zip_text(custom,["INSTRUCTIONS.md","instructions.md","builder/INSTRUCTIONS.md"])
    if not custom_text:
        # fallback: locate any instruction-like md file containing a core marker
        with zipfile.ZipFile(custom) as zf:
            for n in zf.namelist():
                if n.lower().endswith(".md") and "instruction" in n.lower():
                    t=zf.read(n).decode("utf-8", errors="replace")
                    if "SOURCE-APPROVAL-GATE" in t:
                        custom_text=t; break

    reqs=[]
    critical_missing=False
    for cat,rid,title,crit,marker in REQUIREMENTS:
        states={}
        for runtime,text in [("chatgpt_chat",chat_text),("chatgpt_custom",custom_text)]:
            ok=marker in text
            if not ok and crit=="critical": critical_missing=True
            states[runtime]={"state":"equivalent" if ok else "missing","reason":f"Marker {marker} {'present' if ok else 'missing'} in runtime instructions."}
        reqs.append({"category":cat,"id":rid,"title":title,"criticality":crit,"runtime_states":states})

    runtimes={}
    for runtime,text in [("chatgpt_chat",chat_text),("chatgpt_custom",custom_text)]:
        present=sum(1 for m in MARKERS if m in text)
        level="full" if present==len(MARKERS) else ("high" if present>=5 else "moderate")
        rec="publish" if present==len(MARKERS) else "do_not_publish"
        runtimes[runtime]={"level":level,"weighted_score":round(100*present/len(MARKERS),1),"release_recommendation":rec,"notes":[f"{present}/{len(MARKERS)} canonical core markers present in runtime instruction."]}

    payload={"schema_version":2,"reference":{"type":"canonical_contract","description":"Canonical instruction markers and activated runtime contracts in gpt-project.yaml."},"runtimes":runtimes,"requirements":reqs,"notes":["Parity here is behavioral-core parity, not byte-for-byte equality; runtime-specific packaging may differ."]}
    if args.json_out:
        p=root/args.json_out; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    md=["# Runtime parity report","",f"Version: `{args.version}`","","| Runtime | Level | Score | Recommendation |","|---|---|---:|---|" ]
    for k,v in runtimes.items(): md.append(f"| {k} | {v['level']} | {v['weighted_score']:.1f} | {v['release_recommendation']} |")
    md += ["","## Canonical requirements","","| Requirement | Criticality | Chat | Custom GPT |","|---|---|---|---|"]
    for r in reqs:
        md.append(f"| {r['title']} | {r['criticality']} | {r['runtime_states']['chatgpt_chat']['state']} | {r['runtime_states']['chatgpt_custom']['state']} |")
    md += ["","Parity means equivalent core behavior; runtime-specific packaging and Builder guidance may differ."]
    if args.md_out:
        p=root/args.md_out; p.parent.mkdir(parents=True,exist_ok=True); p.write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(payload,ensure_ascii=False,indent=2))
    return 1 if critical_missing or any(v['release_recommendation']=='do_not_publish' for v in runtimes.values()) else 0
if __name__=='__main__': raise SystemExit(main())
