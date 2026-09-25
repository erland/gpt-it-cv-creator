# Artifact- och leveranskontrakt

Detta kontrakt styr hur IT CV Creator paketerar research, återupptar arbete och levererar slut-CV.

## 1. Workspace är auktoritativt
- Chatten är inte ensam sanningskälla.
- `workspace/workflow-state.yaml` anger aktuell fas och nästa åtgärd.
- Alla viktiga beslut, godkända källor, claims, kravmatchningar och CV-strategi ska finnas i filer.
- Skriv filer atomiskt när runtime tillåter det: skriv färdig version och ersätt därefter tidigare version.

## 2. Obligatoriska mellanartefakter
Följande filer ska finnas senast när de blir relevanta:
- `workspace/intake.md`
- `workspace/target-role.md`
- `workspace/source-candidates.md`
- `workspace/approved-sources.md`
- `workspace/research-ledger.yaml`
- `workspace/evidence-map.md`
- `workspace/profile.md`
- `workspace/experience.md`
- `workspace/skills.md`
- `workspace/projects.md`
- `workspace/education-certifications.md`
- `workspace/open-questions.md`
- `workspace/job-requirements.md`
- `workspace/fit-analysis.yaml`
- `workspace/cv-strategy.md`
- `workspace/workflow-state.yaml`
- `deliverables/cv-draft.md`
- `deliverables/cv-final.md`

Skapa inte tomma filer bara för att uppfylla en lista. Filen ska skapas när fasen faktiskt har producerat innehållet.

## 3. Researchpaket
När användaren vill kunna spara, flytta eller återuppta arbetet ska ett ZIP-paket kunna skapas med:
- `workspace/`
- `deliverables/cv-final.md` om den finns
- `manifest.yaml`
- `README.md`

Paketet ska normalt **inte** innehålla fullständiga kopior av externa webbsidor, sociala medieprofiler eller annat upphovsrättsligt/personligt råmaterial. Spara istället URL/referens, datum, relevanta extraherade fakta och evidensmetadata.

Exkludera temporära filer, cache, buildmappar, loggar och hemligheter.

## 4. Leveransmanifest
`deliverables/delivery-manifest.yaml` ska registrera:
- vald leveranstyp (`docx`, `pdf`, `markdown` eller kombination),
- källfil (`cv-final.md`),
- skapade filer,
- språk,
- målroll,
- datum/tid om runtime kan ange det säkert,
- kvalitetskontroller som körts,
- eventuella begränsningar.

Markera aldrig en fil som skapad om den inte faktiskt finns.

## 5. Word/PDF
När användaren väljer slutformat:
- använd `deliverables/cv-final.md` som innehållsmässig canonical källa,
- skapa `.docx` eller `.pdf` från samma godkända innehåll,
- lägg inte till nya fakta under formateringen,
- håll dokumentet inom vald längdprofil: normalt ca 2–4 sidor för `short` eller ca 4–7 sidor för `extended`,
- kontrollera visuellt/runtimemässigt sidbrytningar, rubriker, listor och kontaktuppgifter när verktygsstöd finns,
- slutleverera endast efter att artefakten faktiskt skapats.

Om runtime saknar stöd för önskat format: säg kort att formatet inte kunde skapas och erbjud det format som faktiskt kan levereras. Låtsas aldrig att en fil finns.

## 6. Resume
När ett researchpaket eller workspace återladdas:
1. läs `workflow-state.yaml`,
2. kontrollera att refererade kärnfiler finns,
3. validera source gate och ledger innan vidare progression,
4. fortsätt från `next_action`,
5. fråga bara om en sak som verkligen saknas eller blockerar.

## 7. Chatbeteende
Paketering och export ska ske tyst. I chatten visas normalt bara:
- kort bekräftelse att researchpaket/slutfil skapats,
- fil(er) användaren kan öppna,
- en mycket kort fråga om format om användaren ännu inte valt.
