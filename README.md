# IT CV Creator

IT CV Creator är en stateful research- och CV-assistent för IT-professionella. Den hittar först kandidatens relevanta professionella källor, låter användaren godkänna dem, gör därefter evidensspårbar research och skapar ett målrollsanpassat CV med inledande personligt brev.

## Viktiga egenskaper
- Source approval före deep research.
- Evidensspårning och skydd mot fabricerade meriter.
- Krav-/passformsanalys utan falsk numerisk matchpoäng.
- Kort chat; mellanresultat lagras i workspace.
- 2–4 sidors slutdokument med inledande personligt brev.
- Återupptagningsbart research-workspace.
- Research-ZIP med manifest/checksummor utan råkopior av externa webbsidor.
- Slutleverans som Word eller PDF beroende på användarens val och runtime-stöd.
- Release-readiness med runtime-paritet, hygiene, lint och regressionskontroller.

Se `docs/development-plan.md`, `project-status.yaml` och `assistant/instructions.md`.

## CV-längd

Användaren kan välja `short` (ca 2–4 sidor), `extended` (ca 4–7 sidor) eller `recommended`. Researchen är alltid fullständig; valet styr bara slutdokumentets urval och detaljnivå. `short` är standard.
