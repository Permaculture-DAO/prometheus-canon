---
document_id: PRM-KWX-EXT-CASE-G01@0.2-CANDIDATE
status: RESEARCH_DRAFT_NOT_EXECUTABLE
source_authority: NONE
jurisdiction: TO_BE_DETERMINED_PER_SITE
---
# FASCICOLO 01 — Accordi di gestione forestale, titoli e benefici atmosferici
**Scopo:** strumento di due diligence e scheletro NON VINCOLANTE del futuro *Territorial Stewardship Agreement*. Non è il contratto Kwaxala, non certifica la proprietà della foresta, non crea diritti carbonio e richiede autorità e avvocati competenti.

## 1. Mappa dei diritti: zero equivalenze implicite
| Right ID | Oggetto distinto | Documenti necessari | Stato iniziale |
|---|---|---|---|
| LAND_TITLE | proprietà / concessione / bene pubblico | registro e atti opponibili, titolare, vincoli | UNKNOWN |
| FOREST_TENURE | diritto di taglio / gestione / licenza | testo, scadenza, limiti, cedibilità | UNKNOWN |
| STEWARDSHIP | mandato gestione e obblighi ambientali | accordo firmato, piano, autorità, poteri | UNKNOWN |
| ATMOSPHERIC | attribuzione benefici/diritto crediti | ABA o altro titolo localmente valido | UNKNOWN |
| CARBON_CREDIT | unità certificate con seriale | registro e VVB verificatore | UNKNOWN |
| WATER | accesso, uso, prelievo, scarico | permessi e limitazioni sito | UNKNOWN |
| COMMUNITY | consultazione, consenso, diritti collettivi | accordi comunitari, verbali e poteri | UNKNOWN |
| DATA | dati ecologici, saperi tradizionali, immagini | permessi, licenze, privacy | UNKNOWN |
| CASH | ricavi/royalty/distribuzioni | contratti e libro contabile | UNKNOWN |

**Prova materiale necessaria per ogni riga:** `doc_id`, issuer/titolare, SHA256, data decorrenza/scadenza, identificativo area con CRS e poligono, clausola esatta, diritti di terzi, consenso, custode e reviewer. `UNKNOWN != ZERO` e nessun diritto sorge perché un sensore registra dati.

## 2. Bozza di accordo / articoli (per revisione, non per firma)
**Parti:** [titolare], [comunità / steward], [autorità pubblica], [operatore], [eventuale veicolo], ciascuno con deleghe da verificare.

**Art. 1 — Perimetro e oggetto.** Area [ID], [poligono approvato], [titolo], [uso consentito]; allegare CRS, esclusioni, gravami, servitù, acque, habitat sensibili. Nessuna geometria CAD non registrata prova titoli giuridici.

**Art. 2 — Finalità.** Conservare, rigenerare e monitorare il territorio; metriche ecosistemiche ex ante, stewardship locale e protezioni comunitarie; nessuna garanzia di carbon credit, rendimenti o valore attuale.

**Art. 3 — Poteri e limiti.** Distinguere competenze per opere, specie, manutenzione, censimenti, accesso e raccolta. Modifiche essenziali richiedono permessi e consenso dei soggetti legittimati. Vietati interventi senza titolo.

**Art. 4 — Titoli atmosferici.** Attribuzione dei benefici, esclusività, durata, quote, ulteriori diritti della Corona o dello Stato, project/vintage, registro e autorizzazioni si stabiliscono solo tramite titolo specifico separato. Nessuna cessione tacita.

**Art. 5 — Stewardship e autonomia locale.** Programma annuale, personale locale, approvazione pratiche, diritto a consultazione e opposizione sulle materie riservate, reclami, accesso revisori, protezione dei dati culturali.

**Art. 6 — Spese e flussi.** Fondi filantropici, grant, incassi servizi e ricavi da crediti sono registrati separatamente; debiti, accantonamenti e diritti economici seguono solo la waterfall legale stipulata; nessun cashflow garantito.

**Art. 7 — MRV e dati.** Origine dei campioni, metodo e calibrazione, geolocalizzazione protetta, licenze e verifica indipendente; accesso ai dati con permessi specifici, non pubblicazione dei saperi tradizionali senza consenso.

**Art. 8 — Durata, risoluzione e subentro.** [da definire] coerente con durata titolo e obblighi di permanenza; gestione del danno, finanziamento continuità e rimedi da validare sotto legge applicabile. Il default del fondo non conferisce automaticamente il controllo della foresta.

**Art. 9 — Responsabilità.** Obblighi ambientali, reversals, incendi, danni terzi, assicurazioni e riserve attribuiti da contratti realmente validi. Clausole di esonero non prevalgono su norme inderogabili.

**Art. 10 — Vertenze e audit.** Accesso al reclamo e alla revisione terza; autorità competente, lingua, procedimento e foro validi da scegliere con legale locale.

## 3. Checklist e gate
- T-01 prova titolo e catena storica di trasferimenti.
- T-02 perimetro e servitù indipendentemente verificati.
- T-03 diritto forestale di gestione/estrazione ed eventuale conversione esecutiva.
- T-04 tutela habitat, specie, acqua, lavori e legal compliance.
- T-05 identificazione dei titolari dei benefici atmosferici e periodi sovrapposti.
- T-06 consenso delle comunità effettive, inclusi conflitti tra gruppi legittimati.
- T-07 assenza di garanzie/diritti economici concorrenti non risolti.
- T-08 verifica indipendente di opponibilità, trasferibilità e rischio di insolvenza.

Qualsiasi T richiesto mancante => `RIGHTS_ADMISSIBILITY=HOLD`.

## 4. Benchmark Kwaxala e limiti
Il Governo BC ha istituito nel 2024 la M̓ac̓inuxʷ SFMA (7.865 ha); ciò NON prova fee-simple ownership, entitlements atmosferici specifici o emissione crediti. Il programma canadese federale di miglior gestione **su private land** non va importato come protocollo automaticamente applicabile alla British Columbia. Un'**Atmospheric Benefit Agreement** in BC attribuisce specifici diritti su offset su Crown land; per Kwaxala chiedere atto primario, allegati geografici, date ed eventuali quote, senza inferire dal sito web.

**Fonti primarie:** https://engage.gov.bc.ca/govtogetherbc/engagement/kwiakah-special-forest-management-area/ ; https://www2.gov.bc.ca/gov/content/environment/natural-resource-stewardship/consulting-with-first-nations/first-nations-negotiations/atmospheric-benefit-sharing-agreements ; https://www.kwaxala.com/about .


---
**v0.2 M2 derivative; predecessor:** 01_TITOLI_STEWARDSHIP_ATMOSPHERIC_RIGHTS.md (historical v0.1 preserved unchanged). New annex is analytical and non-executable.

## M2 v0.2 — documentary correction and rights-specific verification
**Evidence grade = OFFICIAL FACT for 7,865-ha designation only.** This confirms a BC-created Special Forest Management Area, NOT fee-simple title, assignment of atmospheric benefits, current carbon-credit issuer, forest-partner equity nor broader 55–57k-ha mandate. This note supersedes any inference otherwise.

**ABA index nuance:** Province publicly lists specific ABA counterparties; Kwiakah was not listed as named individual counterparty on the 2026-01-07 page reviewed, but unpublished/collective/alternative lawful rights are possible. Disposition **UNKNOWN**, not `ABSENT`.

Required Rights Receipt 
- Territory/site identifier and verified cadastral or official polygon including permitted publication level; no inferred coordinates from imagery.
- All rights holders and governing source of legal title, tenure/permit numbers, terms, creditor security, explicit native/Indigenous sovereign claims and dispute mechanism.
- SFMA statutory restriction date and instrument, Tree Farm License (TFL) 45 consequences, permitted activities and historic baseline restrictions.
- Atmospheric benefit instrument (ABA if applicable), all assignors/assignees, term, area, exclusive status, counterclaims and overlapping vintages.
- Whether owners can grant/lease/rescind project access and carbon claim rights; each contract's termination/default survival clauses.
- Counsel's qualified written title opinion and community-issued authority/consent receipt.

**Stop:** no rights-based instrument drafting becomes executable on an AI transcript or a website claim. Keep local First Nation data governed by explicit permission.
