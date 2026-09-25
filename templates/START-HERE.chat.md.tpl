# {{GPT_NAME}} – Chat ZIP

Den här ZIP-filen är den portabla ChatGPT Chat-distributionen för **{{GPT_NAME}}**.

## Användning

Bifoga ZIP-filen i en ChatGPT-konversation och skriv exempelvis: **”Använd denna ZIP som GPT i denna konversation.”**

Assistenten ska därefter följa `assistant/instructions.md`. Den håller normalt chatten kort och visar främst sådant du behöver agera på: källor som ska godkännas, nödvändiga frågor, kort stegstatus och färdiga leveranser.

## Viktiga delar

- `assistant/instructions.md` – runtimeinstruktion
- `assistant/conversation-starters.md` – förslag på startprompter
- `assistant/runtime-contract.json` – kompilerat runtimekontrakt
- `assistant/policies/` – runtimepolicy
- `knowledge/` – CV-, research-, evidens- och leveransregler

Projektets utvecklingsplan, evals, CI-filer och övriga byggartefakter ingår inte i Chat-paketet.

## Version

{{VERSION}}

## Entry point

Detta dokument är den mänskliga entrypointen. `MANIFEST.json` beskriver paketet maskinläsbart.
