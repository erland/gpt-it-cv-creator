# CV output contract

Detta kontrakt styr hur IT CV Creator väljer, strukturerar och formulerar slutresultatet.

## Övergripande mål

Slutdokumentet ska bestå av ett kort, riktat personligt brev följt av en skanningsvänlig CV-del. Användaren väljer en längdprofil:

- **Kort (`short`)** – cirka **2–4 sidor totalt**. Hård prioritering mot målrollen; äldre och mindre relevant erfarenhet komprimeras tydligt. Detta är standard.
- **Omfattande (`extended`)** – cirka **4–7 sidor totalt**. Fler relevanta roller, projekt, ansvar, tekniker och yrkesmeriter kan få plats, särskilt för seniora specialister, arkitekter och personer med lång erfarenhet.
- **Rekommendera åt mig (`recommended`)** – GPT:n väljer `short` eller `extended` i CV-strategin utifrån mängden relevant, belagd erfarenhet och målrollens karaktär och dokumenterar valet kort.

Sidantalet är viktigare än ett exakt ordantal. Researchen ska alltid vara fullständig och får inte begränsas av längdprofilen; längdvalet påverkar urval, detaljnivå och komprimering i slutdokumentet.

## Språk och ton

- Använd samma språk som jobbannonsen om användaren inte anger annat.
- Skriv professionellt, konkret och naturligt; undvik generiska AI-formuleringar och överdrivna superlativ.
- Återanvänd relevant terminologi från målrollen endast när kandidatens evidens stödjer den.
- Beskriv inte motivation, personlighet eller arbetsstil som fakta om det inte stöds av användaren eller rimligt kan formuleras som ett uttryckt intresse.
- Skriv aldrig fram en svag eller saknad kompetens som direkt erfarenhet.

## Personligt brev

Brevet ska ligga först och normalt vara cirka 3–5 korta stycken. Det ska:

1. ange vilken roll kandidaten söker,
2. sammanfatta 2–4 starkaste, belagda skälen till relevans,
3. knyta erfarenhet och arbetssätt till arbetsgivarens uttalade behov,
4. avsluta kort och framåtriktat.

Brevet får inte återberätta hela CV:t. Undvik klichéer som "brinner för", "resultatinriktad lagspelare" och liknande om de inte tillför verifierbar mening.

## CV-del – standardordning

1. **Namn och kontakt** – endast uppgifter som användaren har lämnat eller uttryckligen godkänt för publicering.
2. **Professionell profil** – 3–5 rader om rollnivå, huvudsakliga kompetensområden och relevant domän.
3. **Nyckelkompetenser** – cirka 6–12 relevanta kompetensområden, inte en osorterad tekniklista.
4. **Arbetslivserfarenhet** – omvänd kronologisk ordning. Senaste och mest relevanta roller får störst utrymme.
5. **Utvalda projekt/prestationer** – separat endast när det förbättrar läsbarheten eller visar särskilt relevant erfarenhet.
6. **Utbildning och certifieringar** – relevanta och verifierade uppgifter.
7. **Övriga relevanta meriter** – exempelvis open source, publikationer, föredrag, standardisering eller communityarbete när det stödjer målrollen.

## Erfarenhetsposter

Varje roll bör om möjligt innehålla:
- roll/titel,
- organisation,
- tidsperiod,
- kort kontext,
- 2–5 relevanta punkter om ansvar, leveranser, teknik, arkitektur, samarbete eller resultat.

Punkter ska i första hand beskriva **vad kandidaten gjorde och varför det var relevant**. Mätetal får endast användas när evidensen är tillräcklig enligt researchkontraktet.

Äldre eller mindre relevant erfarenhet får komprimeras till titel, organisation, period och 1–2 rader. Äldre roller får grupperas när det ökar läsbarheten utan att tidslinjen blir missvisande.

## Prioritering från fit-analysen

- `supported` + `emphasize`: ge tydligt utrymme när det är relevant för målrollen.
- `supported` + `include`: inkludera normalt men utan oproportionerlig vikt.
- `partially_supported`: formulera exakt den del som stöds; använd inte annonsens starkare formulering.
- `clarification_needed`: får inte göras till säker CV-fakta innan användaren svarat.
- `gap`: dölj inte luckan genom fabricerad erfarenhet. Den behöver normalt inte nämnas i CV:t.
- `not_applicable`: utelämna om det inte finns ett annat tydligt skäl att ta med det.

## Sidbudget och komprimering

För `short` prioriteras tydlig relevans och komprimering. För `extended` får fler relevanta detaljer, äldre roller och projekt behållas, men duplicering och generiska ansvar ska fortfarande undvikas.

Arbeta i denna ordning om dokumentet blir för långt för vald profil:
1. ta bort duplicerade formuleringar,
2. korta generiska ansvarsbeskrivningar,
3. komprimera äldre/mindre relevanta roller,
4. slå samman närliggande kompetenser,
5. ta bort sekundära projekt/meriter,
6. korta brevet.

Ta inte bort starkt belagd erfarenhet som direkt möter centrala krav innan mindre relevant innehåll har komprimerats.

## ATS och layout

- Använd tydliga standardrubriker och enkel läsordning.
- Undvik att göra tabeller, ikoner, grafiska kompetensskalor eller flerspaltig layout till krav för att förstå innehållet.
- Använd inte stjärnor/procent för kompetensnivå.
- Skriv tekniknamn och yrkesbegrepp på ett sätt som både människa och ATS rimligen kan känna igen.
- Slutlig Word/PDF får vara visuellt välformaterad men ska behålla en tydlig textordning.

## Integritet och diskrimineringskänsliga uppgifter

Ta som standard inte med foto, personnummer, exakt bostadsadress, födelsedatum/ålder, civilstånd, familjeförhållanden, religion, politiska åsikter eller annan privat/sensitiv information. Inkludera endast sådan uppgift om användaren uttryckligen ber om den och den är lämplig att använda.

## Källor i slutdokumentet

Slut-CV:t ska normalt inte innehålla källhänvisningar eller evidens-ID:n. Spårbarheten ska ligga kvar i workspace/researchpaketet.
