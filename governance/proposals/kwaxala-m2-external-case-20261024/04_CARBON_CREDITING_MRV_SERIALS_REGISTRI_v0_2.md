---
document_id: PRM-KWX-EXT-CASE-G04@0.2-CANDIDATE
status: RESEARCH_PROTOCOL_NO_CREDIT_AUTHORITY
source_authority: NONE
---
# FASCICOLO 04 — Crediti carbonio, MRV, registri, seriali, verifiche indipendenti
**Oggetto:** pipeline di prova; non è una metodologia registrata, né il registro effettivo di Kwaxala. La tutela legale, la stima del carbonio e l'emissione di un credito sono eventi distinti.

## A. Selezione metodologia e giurisdizione
- Stabilire tipo terreno (BC Crown/private/other), diritto territoriale, mandato del proponente, ABA/benefits rights e relative date; le regole carbonio cambiano fra giurisdizioni.
- Fissare programma e versione del protocollo **formalmente ammissibile**; non applicare automaticamente il protocollo federale canadese per *Improved Forest Management on private land* alla BC Crown land. L'overview federale esclude BC.
- Registrare autorità, project developer, FPIC/consenso applicabile, eligible activities, periodo, pools, baseline, leakage, permanenza e metodo di calcolo, VVB indipendente.

## B. Chronology & additionality
`progetto ipotizzato → diritto di gestione → legal protection effective → project start metodologico → baseline freeze → validazione → monitoraggio → verifica → issuance → vendita/trasferimento → retirement`. Una restrizione di taglio già vigente cambia il controfattuale: vietato trattare indefinitamente lo scenario pre-protezione come baseline legale senza approvazione metodologica. Devono essere affrontati i test di additionalità, leakage, permanence, doppio conteggio e strumenti nazionali applicabili.

## C. Data contract carbon
`project_id, registry_url, methodology_id/version, geofence_sha, tenure_sha, atmospheric_benefit_sha, validation_vvb, verification_vvb, monitor_period_start/end, baseline_version_sha, independently_verified_tco2e, buffer_units, issued_units, serials, ownership_account, sold_units, retired_units, reversal_debits, claim_beneficiary, disclosure_state`.

**Vincoli:** `issued <= verified net eligible under applicable rules`; un seriale `RETIRED` non si rivende; `SOLD != RETIRED != ISSUED != VALIDATED`; nessuna cifra `UNKNOWN` trattata come zero. Vietato fabbricare seriali o caricarli in un registro pubblico senza autorizzazione.

## D. Standard di misura e QA
Campioni stratificati realmente indipendenti, strumenti calibrati, fattori di biomassa/versioni, suolo se protocollo lo include, disturbi, deadwood e altri pools ammessi; telerilevamento con limiti. Un soggetto terzo deve eseguire verifica e report firmato con metodo. L'evidenza di biodiversità, acqua e benessere comunitario ha proprie metriche e non genera automaticamente `tCO2e` o crediti biodiversità.

**Test automatici locali SHADOW:** duplicazione seriali, gap geospaziali, sovrapposizione area/anni, livello di incertezza, titolo scaduto, issuer irregolare, crediti sold+retired incoerenti, documenti VVB mancanti, emissione prima del processo metodologico ammissibile, reversal non gestito. Problemi => `HOLD_CREDIT_CLAIM`, senza alterazione dei registri ufficiali.

## E. Allegato registro eventi
`CARBON_REGISTRY_LEDGER_TEMPLATE.csv` contiene sole intestazioni, nessuna emissione reale. Chi documenta una riga deve allegare URI ufficiale, data scarico, hash dei documenti, timestamp, reviewer e licenze. Se il seriale non risulta registrato: `NOT_VERIFIED`, non `CREDIT_EXISTING`.

## F. Richieste specifiche per Kwaxala
Richiedere progetto e programma registrato, accordo atmosferico applicabile al perimetro M̓ac̓inuxʷ, titolarità sui seriali, primo vintage ammissibile post-protezione 2024, relazioni di verifica e di eventuale emissione, compratori e prova distribuzione. Se gli atti non sono divulgabili, classificarli come `PRIVATE_PENDING_CUSTODIAN_ACCESS`, non dichiararli inesistenti.

**Fonti:** https://icvcm.org/core-carbon-principles/ ; https://www2.gov.bc.ca/gov/content/environment/climate-change/industry/offset-projects/offset-protocols ; https://www2.gov.bc.ca/gov/content/environment/natural-resource-stewardship/consulting-with-first-nations/first-nations-negotiations/atmospheric-benefit-sharing-agreements ; https://www.canada.ca/en/environment-climate-change/services/climate-change/pricing-pollution-how-it-will-work/output-based-pricing-system/federal-greenhouse-gas-offset-system/overview-improved-forest-management-private-land.html .


---
**v0.2 M2 derivative; predecessor:** 04_CARBON_CREDITING_MRV_SERIALS_REGISTRI.md (historical v0.1 preserved unchanged). New annex is analytical and non-executable.

## M2 v0.2 — jurisdiction-accurate BC methodology audit
BC's public **Forest Carbon Offset Protocol (FCOP)** is an approved provincial methodology category, potentially applicable depending on eligible project type and legally verified site; **do not state Kwaxala is registered under it**. A provincially created SFMA may modify regulatory additionality and permitted counterfactual from the effective date **2024-05-24**. The correct project-specific grandfathering and method version requires an accredited specialist decision; do not import US, EU or privately owned forest rules.

Hard prerequisite ledger: (A) legal rights/ABA, (B) project public registry ID + proponent, (C) methodology and version, (D) project start and baseline start, (E) project/creditable polygon and authority, (F) independent validation/verifier and verification-period reports, (G) leakage/permanence/reversal and reserve/buffer, (H) issued credit serial ranges, (I) cash-sale/retirement record, (J) claims made by each buyer. No automatic offset status from narrative.

**No-double-claim invariants:** one serial has one state per registry and as-of snapshot; contractual transfer does not imply environmental retirement; no independently unverified backdating; no carbon benefit converted to habitat/Centree PRU unit or token at fixed par. Missing registry reference => `ISSUANCE_UNVERIFIED`.

**Threat model:** selective plots, cherry-picked vintages, stale baseline after protection, non-additional avoided emissions, leakage into neighboring forests, reversal, offset sold twice, false claims of avoided social harm or Indigenous consent, and marketing beyond quantification protocol. Independent verification does not absolve claim-makers of liability.
