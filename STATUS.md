# Status

Steg 11 – GitHub CI och release är klart och validerat.

Verifierat:
- CI kör explicit distributionsbygge samt full release-readiness,
- CI sparar valideringsrapporter som Actions-artifact,
- GitHub Release härleder semantisk version från release-taggen,
- både `0.1.0` och `v0.1.0` stöds och ger version `0.1.0`,
- ogiltiga release-taggar stoppas,
- releasekandidaten kör samma release-readiness-gates som lokal validering,
- SHA256SUMS.txt verifieras före release-uppladdning,
- lokal 0.1.0-kandidat: READY, distribution validation PASS, checksums PASS.

Utvecklingsplanens steg 0–11 är slutförda. Projektet är redo att läggas i ett GitHub-repo och publiceras som release 0.1.0.

- 0.1.1: configurable CV length profiles (`short`, `extended`, `recommended`) added; research remains full-depth independent of output length.
- 0.1.1 regression verified: ~2,900-word draft rejected by `short` and accepted by `extended`; `recommended` must resolve before drafting.
- Release readiness for 0.1.1: READY, no warnings or blockers.
