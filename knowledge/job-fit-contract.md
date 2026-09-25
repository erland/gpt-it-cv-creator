# Jobb- och passformsanalys – kontrakt

## Syfte

Översätt en jobbannons eller målroll till en strukturerad kravbild och koppla den mot kandidatens belagda erfarenhet. Analysen ska styra urval och betoning i CV:t utan att skapa kvalifikationer som saknar stöd.

## Kravmodell

Varje krav får ett stabilt ID (`REQ-001`, `REQ-002`, ...). Dokumentera:

- `category`: `must`, `merit`, `responsibility`, `domain`, `technical`, `leadership`, `collaboration`, `language`, `education`, `other`
- `requirement`: kort normaliserad formulering
- `evidence_in_ad`: kort hänvisning/parafras till annonsen eller användarens rollbeskrivning
- `priority`: `explicit_must`, `explicit_merit`, `implied_core`, `contextual`
- `keywords`: relevanta ord/begrepp som naturligt kan återanvändas om kandidaten har stöd för dem
- `notes`: tolkningsrisk eller oklarhet

Krav får inte uppfinnas från stereotypa antaganden om en titel. Om målrollen bara beskrivs av användaren ska krav som inte uttryckligen angetts markeras som `contextual` och inte behandlas som formella krav.

## Matchmodell

Varje krav kopplas till kandidatens evidens med ett statusvärde:

- `supported`: tydligt belagt
- `partially_supported`: relevant men ofullständigt belagt
- `clarification_needed`: sannolik relevans men användaren behöver bekräfta något väsentligt
- `gap`: inget tillräckligt stöd
- `not_applicable`: kravet bedöms inte behöva speglas i CV:t

För varje matchning dokumenteras:

- `requirement_id`
- `status`
- `claim_ids`: noll eller flera claim-ID:n från `research-ledger.yaml`
- `evidence_summary`: kort saklig förklaring
- `cv_action`: `emphasize`, `include`, `compress`, `omit`, `ask_user`
- `wording_guardrail`: vad CV:t får säga utan att gå längre än evidensen

## Hårda regler

1. `supported` kräver minst ett användbart claim-ID med tillräcklig evidens.
2. `partially_supported` får inte formuleras som full uppfyllelse i CV:t.
3. `clarification_needed` ska skapa en fråga endast om svaret materiellt påverkar CV:t.
4. `gap` får aldrig maskeras genom synonymbyte eller överdriven formulering.
5. Ett krav i annonsen är inte evidens för att kandidaten har kompetensen.
6. När annonsen nämner ett verktyg/ramverk som kandidaten inte har belagt, får närliggande teknik inte automatiskt likställas med detta.
7. Överförbara erfarenheter får användas, men ska beskrivas som just överförbara erfarenheter – inte som direkt erfarenhet av saknad teknik/domän.
8. Mätbara påståenden följer research-evidenskontraktets hårdare krav.
9. Använd inte numerisk totalpoäng eller procentuell passform som om den vore objektiv sanning.
10. CV:t ska prioritera de mest relevanta belagda erfarenheterna, inte försöka täcka varje krav till varje pris.

## CV-strategi från analysen

Prioritera i denna ordning:

1. `explicit_must` + `supported`
2. `explicit_merit` + `supported`
3. `implied_core` + `supported`
4. relevanta `partially_supported` där formuleringen kan vara exakt
5. överförbara erfarenheter som förklarar en verklig närliggande styrka

`gap` ska normalt inte nämnas i CV:t. Om luckan är central och sannolikt behöver hanteras i ansökan kan strategin föreslå en saklig formulering om närliggande erfarenhet eller lärandeförmåga, utan att påstå kompetens som saknas.

## Compact chat

Jobb- och fit-analysen skrivs till workspace. Visa den inte utförligt i chatten om användaren inte ber om det. Fråga endast om blockerande eller materiella oklarheter.
