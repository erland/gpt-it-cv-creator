# Research- och evidenskontrakt

Detta kontrakt styr deep research efter SOURCE-APPROVAL-GATE.

## 1. Identitetsnivå
Varje extern källa ska ha en identitetsbedömning:
- `confirmed`: direkt länkad av kandidaten eller flera starka oberoende signaler.
- `probable`: flera rimliga signaler men inte fullt bekräftad.
- `uncertain`: otillräckligt underlag eller konflikt.

`uncertain` får inte användas som faktaunderlag utan användarens uttryckliga korrigering/bekräftelse. `probable` får endast användas försiktigt när användaren har godkänt just källan och ingen konflikt finns.

## 2. Källklass
Klassificera källan:
- `user_provided`: användaren själv eller fil/länk användaren uttryckligen lämnat.
- `first_party`: kandidatens egen professionella profil, portfolio, repository eller publikation.
- `official_third_party`: arbetsgivare, konferens, certifieringsutfärdare, standardiseringsorgan, projektorganisation eller liknande officiell källa.
- `credible_secondary`: trovärdig sekundärkälla.
- `weak_secondary`: aggregator, automatgenererad profil eller annan svag källa.

Prioritera i denna ordning: `user_provided` → `first_party` → `official_third_party` → `credible_secondary`. `weak_secondary` ska normalt bara användas för discovery, inte som ensam grund för CV-fakta.

## 3. Claim-typer
Varje central uppgift registreras som claim med stabilt ID. Exempel:
- anställning/roll,
- tidsperiod,
- ansvar,
- teknik/kompetens,
- projekt eller produkt,
- resultat/effekt,
- utbildning/certifiering,
- publikation/föredrag/open source.

## 4. Evidensstyrka
Tillåtna nivåer:
- `direct`: uppgiften står uttryckligen i en stark källa eller har lämnats av användaren.
- `corroborated`: stöds av minst två oberoende relevanta källor.
- `supported`: rimligt tydligt stöd men mindre direkt.
- `inferred`: redaktionell slutsats från fakta; får inte skapa ny merit.
- `uncertain`: otillräckligt eller motstridigt stöd.

Endast `direct`, `corroborated` och normalt `supported` får användas som säkra CV-fakta. `inferred` får användas för formulering/struktur men inte som ny faktisk merit. `uncertain` ska utelämnas eller föras till clarification.

## 5. Konflikter
Om källor skiljer sig åt om datum, titel, arbetsgivare, ansvar eller resultat:
1. registrera konflikten; skriv inte över den,
2. prioritera kandidatens uttryckliga korrigering och starkare förstahandskälla,
3. be användaren om förtydligande om konflikten påverkar CV:t,
4. använd inte en exakt uppgift som fortfarande är omtvistad.

En svag sekundärkälla ska inte väga tyngre än kandidatens eget material eller officiell källa utan tydlig anledning.

## 6. Resultat och siffror
Mätbara resultat, procentsatser, besparingar, antal användare/team/system eller andra siffror kräver `direct` eller `corroborated` evidens. Om siffran inte kan styrkas: skriv om kvalitativt eller utelämna.

## 7. Kompetensbevis
En teknik får tas med som faktisk kompetens när minst ett av följande finns:
- användaren uppger den,
- explicit yrkesroll/projekt beskriver användning,
- kod/repository eller publikation ger tydligt stöd,
- certifiering styrker relevant kunskap.

Enstaka omnämnande, stjärnmarkering, följande av konto eller dependency i ett projekt räcker inte ensamt för att hävda kompetens.

## 8. Chattyta
Researchartefakter skrivs i workspace och ska inte dumpas i chatten. Visa endast:
- källor som väntar på beslut,
- konflikter/osäkerheter som kräver användarens svar,
- mycket kort stegstatus,
- slutleverans och formatval.
