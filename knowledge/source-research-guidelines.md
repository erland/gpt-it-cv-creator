# Källresearch för IT CV Creator

Denna fil beskriver vilka professionella källtyper som kan vara relevanta under den ytliga källkartläggningen. Alla externa personkällor omfattas av SOURCE-APPROVAL-GATE.

## Prioritetsordning

1. Kandidatens eget material och länkar som kandidaten själv lämnat.
2. Förstahandskällor som kandidaten själv kontrollerar eller där kandidaten tydligt är namngiven.
3. Officiella arbetsgivar-, projekt-, konferens-, publikations- eller communitykällor.
4. Trovärdiga sekundärkällor som kan styrka en yrkesrelevant uppgift.

## Relevanta källtyper

### Professionella profiler och portfolio
- LinkedIn.
- Personlig webbplats, portfolio eller teknisk blogg.
- GitHub, GitLab, Bitbucket och andra kodplattformar.
- Stack Overflow/Stack Exchange när profilen går att identitetsmatcha.
- Yrkesrelevanta Mastodon-, Bluesky- eller andra sociala profiler där innehållet faktiskt visar professionell aktivitet.

### Kod, paket och open source
- Repositories, commits, issues, pull requests och releasehistorik där kandidatens bidrag kan beläggas.
- Maven Central, npm, PyPI, NuGet, crates.io, RubyGems eller motsvarande paketregister när kandidaten kan kopplas till paketet.
- OpenSSF, CNCF, Apache, Eclipse, Linux Foundation och andra open-source/communitysidor som dokumenterar roller eller bidrag.

### Föredrag, communities och publikationer
- Konferensprogram, speaker-profiler och inspelade föredrag.
- Meetup- och communitysidor för arrangörs- eller talarroller.
- Artiklar, whitepapers, böcker och tekniska publikationer.
- ORCID, Google Scholar, universitet/research portals och DOI-index när akademiska meriter är relevanta.
- Patentdatabaser när patent eller uppfinningar är yrkesrelevanta och identiteten är säker.

### Arbete, projekt och professionella meriter
- Arbetsgivares officiella profilsidor, case studies och pressmeddelanden.
- Projektsidor och offentliga produkt-/tjänstesidor som kan styrka projektets existens och kandidatens roll när den uttryckligen framgår.
- Professionella föreningar, standardiseringsorgan och arbetsgrupper, till exempel IETF, W3C, ISO-relaterade grupper eller nationella branschorganisationer.
- Certifieringsutfärdares publika verifieringssidor när kandidaten själv har lämnat verifieringslänk eller identiteten annars är säker.
- Offentliga upphandlings-, myndighets- eller organisationsdokument endast när de har tydlig yrkesrelevans och inte exponerar onödiga personuppgifter.

## Källor som normalt inte ska användas

- Privata sociala mediekonton, familjeuppgifter eller privatliv.
- Personregister, adressregister, personsöktjänster eller datamäklare.
- Uppgifter om hälsa, religion, politik, facklig tillhörighet, sexliv, etnicitet eller andra känsliga personuppgifter.
- Bilder, forumrykten eller osignerade sammanställningar utan tydlig professionell relevans.
- Automatiskt genererade profilsidor som bara skrapar andra tjänster, om en bättre förstahandskälla finns.

## Identitetsmatchning

Använd flera oberoende signaler när en källa inte är direkt länkad av kandidaten, till exempel:
- arbetsgivare och tidigare arbetsgivare,
- geografisk region på grov nivå,
- tekniskt område eller projektnamn,
- användarnamn som återkommer mellan profiler,
- länkar mellan profiler,
- sammanhängande tidslinje.

Ett namn ensamt räcker inte. Vid rimlig osäkerhet: märk källan `identity_uncertain` och låt användaren avgöra om den tillhör rätt person.

## Discovery kontra deep research

Discovery får endast samla metadata som behövs för att användaren ska kunna avgöra om källan är relevant och tillhör rätt person: namn, URL, källtyp, kort beskrivning, identitetssignaler och osäkerhet.

Deep research får börja först när `source_gate.approval_complete=true`. Endast `approved_source_ids` får analyseras på djupet.
