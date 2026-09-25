# IT CV Creator – utvecklingsplan

## Mål

Skapa en GPT som hjälper en person inom IT att ta fram ett trovärdigt, tjänsteanpassat CV på 2–4 sidor. Resultatet ska inledas med ett personligt brev och därefter ge en strukturerad beskrivning av kompetens och erfarenhet. GPT:n ska arbeta källbaserat, låta användaren godkänna källor innan djupanalys och kunna leverera slutresultatet som Word eller PDF.

## Rekommenderad projektprofil

- Profil: `workflow_research_heavy`
- Modellrobusthet: `stateful`
- Skäl: flerstegsresearch, användargodkända källor, återupptagning, evidensspårning, mellanartefakter och slutgenerering.

## Kärnprinciper

1. Sök först efter möjliga källor men gör ingen djup profilering innan användaren har godkänt dem.
2. Be alltid om jobbannons eller beskrivning av tjänst/roll som CV:t ska riktas mot.
3. Fråga efter ytterligare underlag som användaren själv vill tillföra, exempelvis befintligt CV, projektlista, certifieringar, utbildningar, presentationer, publikationer eller privata anteckningar.
4. Använd endast relevanta och rimligt tillförlitliga källor som underlag för faktiska påståenden.
5. Hitta inte på erfarenheter, roller, resultat, tekniker, utbildningar, certifieringar eller prestationer.
6. Anpassa urval, ordning, formulering och betoning till tjänsten utan att förvanska personens bakgrund.
7. Märk osäkra eller motstridiga uppgifter och be användaren bekräfta dem innan de används som fakta i slutresultatet.
8. Håll en käll-/evidenskarta så att varje viktig sakuppgift i CV-underlaget kan spåras tillbaka till en eller flera godkända källor.
9. Slut-CV:t ska inte innehålla källhänvisningar om användaren inte uttryckligen vill ha det; evidenskartan bevaras separat.
10. Behandla sociala medier selektivt: prioritera yrkesrelevant och offentligt material och undvik privat eller känslig information som inte behövs för CV:t.

## Föreslaget arbetsflöde

### State 1 – Intake

Samla in:
- personens namn eller annan identifiering som behövs för att hitta rätt person,
- jobbannons, länk eller beskrivning av önskad roll,
- eventuellt befintligt CV,
- övrigt material som användaren vill tillföra,
- eventuella källor användaren uttryckligen vill inkludera eller exkludera.

Utdata:
- `workspace/intake.md`
- `workspace/target-role.md`

Gate:
- målrollen är tillräckligt beskriven för att styra research och CV-anpassning.

### State 2 – Source discovery

Sök brett men ytligt efter kandidat-källor, exempelvis:
- LinkedIn,
- GitHub och andra kodplattformar,
- personlig webbplats,
- blogg,
- företags-/organisationssidor,
- konferens- och presentationssidor,
- publikationer,
- relevanta professionella sociala mediekonton,
- andra tydligt yrkesrelaterade offentliga källor.

För varje källa dokumenteras:
- URL,
- källtyp,
- varför den sannolikt tillhör rätt person,
- varför den kan vara relevant,
- preliminär tillförlitlighet,
- eventuella identitets-/matchningsrisker.

Utdata:
- `workspace/source-candidates.md`

Gate:
- användaren måste uttryckligen godkänna vilka källor som får användas i djupanalysen.

### State 3 – Source approval

Presentera kandidat-källorna kompakt och låt användaren:
- godkänna,
- avvisa,
- lägga till,
- korrigera felaktig personmatchning.

Utdata:
- `workspace/approved-sources.md`

Gate:
- minst en tillräcklig uppsättning källor är godkänd eller användaren har valt att fortsätta med eget material.

### State 4 – Deep research

Analysera alla godkända källor i ett eller flera steg. Extrahera endast yrkesrelevant information, exempelvis:
- anställningar och roller,
- ansvar,
- projekt,
- tekniker och verktyg,
- arkitektur-/utvecklingsområden,
- ledarskap och samarbete,
- branscher och domäner,
- utbildning,
- certifieringar,
- publikationer och presentationer,
- open-source-bidrag,
- resultat och prestationer när de faktiskt stöds av underlaget.

Utdata kan delas upp i:
- `workspace/profile.md`
- `workspace/experience.md`
- `workspace/skills.md`
- `workspace/projects.md`
- `workspace/education-certifications.md`
- `workspace/evidence-map.md`
- `workspace/open-questions.md`

Gate:
- alla relevanta godkända källor är analyserade,
- motstridigheter och väsentliga luckor är identifierade.

### State 5 – Clarification

Fråga användaren endast om sådant som materially påverkar CV:t, exempelvis:
- oklar tidslinje,
- vilken roll i ett projekt personen faktiskt hade,
- resultat som inte kan verifieras,
- vilka äldre erfarenheter som ska prioriteras,
- saknade kontaktuppgifter eller språk.

Uppdatera workspace-filerna med bekräftade uppgifter.

Gate:
- inga väsentliga oklarheter återstår som riskerar att skapa ett missvisande CV.

### State 6 – Target-role analysis

Analysera jobbannonsen/rollen och skapa en kravprofil:
- måste-krav,
- meriterande krav,
- tekniska kompetenser,
- domänkompetens,
- ansvarsnivå,
- ledarskap/samarbete,
- nyckelord,
- sannolika prioriteringar i urvalet.

Matcha kandidatens belagda erfarenheter mot kravprofilen utan att skapa obelagda påståenden.

Utdata:
- `workspace/job-requirements.md`
- `workspace/fit-analysis.md`

### State 7 – CV strategy

Bestäm:
- vilka erfarenheter som ska få mest utrymme,
- vilka äldre/irrelevanta detaljer som ska kortas,
- vilken yrkesprofil som ska lyftas fram,
- vilka konkreta exempel som bäst visar passform,
- vilka ord och begrepp från annonsen som naturligt kan återanvändas.

Utdata:
- `workspace/cv-strategy.md`

### State 8 – Draft

Skapa ett första komplett utkast på 2–4 sidor med:
1. personligt brev,
2. kort professionell profil,
3. nyckelkompetenser,
4. arbetslivserfarenhet,
5. utvalda projekt/prestationer när relevant,
6. utbildning och certifieringar,
7. övriga relevanta meriter.

Prioritera läsbarhet, konkretion och relevans för målrollen framför maximal detaljmängd.

Utdata:
- `deliverables/cv-draft.md`

### State 9 – Quality review

Kontrollera:
- att inga fakta saknar stöd eller användarbekräftelse,
- att tidslinjen är konsekvent,
- att personligt brev och CV är tydligt riktade mot målrollen,
- att överdrifter och generiska AI-formuleringar har minimerats,
- att dokumentet håller sig inom 2–4 sidor efter normal layout,
- att relevanta krav från jobbannonsen täcks där kandidaten faktiskt har stöd för dem,
- att känslig eller privat information inte tagits med utan tydligt behov.

### State 10 – Delivery

Fråga användaren om önskat slutformat om det inte redan är angivet:
- Word (`.docx`)
- PDF (`.pdf`)

Erbjud även ett researchpaket som ZIP med exempelvis:
- godkända källor,
- strukturerad profil,
- evidenskarta,
- kravanalys,
- CV-strategi,
- slutlig Markdown-version.

Denna ZIP ska inte innehålla råkopior av tredjepartsinnehåll när det inte behövs; lagra hellre länkar, egna sammanfattningar och evidensnoteringar.

## Föreslagen workspace-struktur

```text
workspace/
  intake.md
  target-role.md
  source-candidates.md
  approved-sources.md
  profile.md
  experience.md
  skills.md
  projects.md
  education-certifications.md
  evidence-map.md
  open-questions.md
  job-requirements.md
  fit-analysis.md
  cv-strategy.md
  workflow-state.yaml

deliverables/
  cv-draft.md
  cv-final.md
  cv-final.docx | cv-final.pdf
```

## Viktiga funktionella kontrakt

### Research
- webbsökning krävs,
- användargate före djupanalys,
- identitetsmatchning måste redovisas,
- endast godkända källor får användas i fördjupad profilering.

### Evidence
- varje central erfarenhet/kompetens ska kunna kopplas till källa eller explicit användaruppgift,
- osäker information får inte omvandlas till säker CV-fakta,
- konflikter mellan källor ska flaggas.

### CV-anpassning
- optimera relevans och presentation,
- aldrig uppfinna eller förstärka fakta bortom underlaget,
- prioritera belagda erfarenheter som svarar mot jobbkraven.

### Artifact
- arbetsunderlag i Markdown,
- resumable state i strukturerad fil,
- researchpaket som ZIP,
- slutleverans som DOCX eller PDF.

## Runtime-bedömning

| Runtime | Suitability | Aktivera som standard | Motivering |
|---|---|---:|---|
| ChatGPT Chat | hög | ja | Passar interaktiv research, källgodkännande, filer och stegvis arbete. |
| ChatGPT Custom | hög | ja | Bra slutanvändarformat för själva IT CV Creator och stödjer ett styrt samtalsflöde. |
| Claude Projects | medel/hög | nej | Kan bära stora delar av canonical-flödet men fil-/webb-/artefaktbeteende kan skilja sig och bör valideras separat. |
| OpenCode | reducerad | nej | Tekniskt möjligt men dåligt anpassat till den primära målgruppen och dokumentflödet. |
| OpenAI Plugin | reducerad | nej | Skills kan återanvända delar av logiken, men persistent research/workspace och full dokumentleverans är inte likvärdigt med huvudflödet. |

## Utvecklingssteg

### Steg 1 – Canonical projektgrund
Skapa projektstruktur, `gpt-project.yaml`, `project-status.yaml`, `PROJECT.md`, `README.md` och canonical instruktion.

Klart när:
- kärnsyfte, målgrupp, input/output och begränsningar är kodifierade,
- stateful-robusthet och workflow-state finns i projektkontraktet.

### Steg 2 – Workflow och state
Implementera states, gates, resume-logik och `workflow-state.yaml`.

Klart när:
- GPT:n inte kan hoppa över användarens godkännande av källor,
- ett avbrutet arbete kan återupptas från strukturerad status.

### Steg 3 – Research- och källkontrakt
Definiera source discovery, identitetsmatchning, source approval, deep research och evidence-map.

Klart när:
- källor kan hittas, bedömas, godkännas och spåras deterministiskt i workflowet.

### Steg 4 – Jobb- och passformsanalys
Definiera kravanalys av jobbannons/roll samt regler för evidensbaserad matchning.

Klart när:
- GPT:n kan prioritera relevanta erfarenheter utan att hitta på kvalifikationer.

### Steg 5 – CV- och brevstruktur
Skapa mallar och instruktioner för 2–4 sidors CV med inledande personligt brev.

Klart när:
- innehållsordning, längdregler, ton och kvalitetskriterier är definierade.

### Steg 6 – Workspace- och artifact-hantering ✅
Implementera Markdown-mellanartefakter, research-ZIP och leveranskontrakt för DOCX/PDF.

Implementerat:
- komplett workspace-mall för intake, målroll, research och CV-strategi,
- artifact-/leveranskontrakt med canonical `cv-final.md`,
- research-ZIP med manifest och SHA-256 för inkluderade filer,
- exkludering av råa externa webbsidor, temporära filer och uppenbara hemligheter,
- delivery manifest som inte får hävda att en fil finns om den saknas,
- regler för återupptagning från workspace och kort chat vid export.

Klart när:
- hela processen kan inspekteras och återupptas via filer,
- slutformat kan väljas av användaren.

### Steg 7 – Tester och modellkompatibilitet
Skapa evals för bland annat:
- fel person i sökresultat,
- avvisad källa,
- motstridiga uppgifter,
- saknad jobbannons men beskriven målroll,
- obelagd kompetens i jobbannonsen,
- återupptagning mitt i research,
- användare som vill lägga till eget material sent i processen,
- korrekt terminal behavior efter färdig leverans.

### Steg 8 – ChatGPT Chat-distribution
Bygg och validera Chat ZIP från canonical projekt.

### Steg 9 – ChatGPT Custom-distribution
Kompilera och validera Custom GPT-distribution med plattformsanpassade instruktioner och Knowledge endast där det behövs.

### Steg 10 – Runtime parity, hygiene och release readiness ✅
Kontrollera canonical parity mellan de två aktiverade runtime-målen, project hygiene, lint, tester och release readiness.

Implementerat:
- deterministisk parity-validator för aktiverade runtimes,
- sex canonical kärnregler verifieras i både Chat och Custom GPT,
- final hygiene från ren källa,
- samlad release-readiness-gate som bygger om kandidaten före runtimekontroller,
- persistenta parity- och readiness-rapporter.

Klart när:
- båda aktiverade runtimes har full kärnparitet,
- inga blockerare eller warnings återstår i release-readiness.

### Steg 11 – GitHub CI och release ✅
Aktivera GitHub Actions för validering och release-byggning. Versionsnumret ska härledas från release-taggen.

Klart när:
- projekt-ZIP och aktiverade distributioner kan byggas reproducerbart från GitHub Release.

Verifierat:
- CI kör explicit build samt full release-readiness och distributionsvalidering,
- release-taggar `1.2.3` och `v1.2.3` normaliseras till versionsnumret `1.2.3`,
- ogiltiga taggformat avvisas,
- releaseflödet verifierar `SHA256SUMS.txt` före uppladdning,
- lokal releasekandidat 0.1.0 passerar readiness, distribution validation och checksum-kontroll.
