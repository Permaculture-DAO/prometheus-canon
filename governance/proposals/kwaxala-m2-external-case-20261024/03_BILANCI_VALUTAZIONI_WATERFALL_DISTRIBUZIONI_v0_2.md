---
document_id: PRM-KWX-EXT-CASE-G03@0.2-CANDIDATE
status: ACCOUNTING_AND_VALUATION_TEMPLATE_NO_FINANCIAL_OFFER
source_authority: NONE
---
# FASCICOLO 03 — Bilanci, valutazioni, waterfall, storico distribuzioni
**NON contiene bilanci, prezzi pagati, distribuzioni o valutazioni effettivamente verificate di Kwaxala**. È la struttura dei prospetti da redigere per PROMETHEUS usando atti primari, revisione contabile e perito terzo. I ricavi futuri non sono cash; gli indici ecologici non sono attivi contabili per definizione.

## A. Perimetro e data del bilancio
Una riga per entità reale: `rights_holder`, `local_steward`, `site_project`, `shared_service_provider`, `fund/issuer_optional`. Identificare consolidamento e parti correlate secondo i principi contabili realmente applicabili. Per ogni voce: periodo, valuta, criterio recognition, contropartita, fattura/registro, flusso banca, contratto, revisore, stato.

**Conto economico**: ricavi da crediti consegnati secondo policy; ricavi da servizi ecosistemici effettivamente venduti; grant soggetti a riconoscimento; OPEX forest keeper e lavori; costi MRV/VVB/registry; piattaforma/fee; ammortamenti; impairment, interessi e tributi. Ogni grandezza con `realised`, `accrued`, `forecast` e `unknown` differenti.

**Situazione patrimoniale**: cassa disponibile/vincolata; crediti contrattuali, non presunti; impianti e diritti immateriali solo se iscrivibili; debiti, grants vincolati, riserve per reversal, anticipi dei compratori, passività da cause e fondi. Separare valore d'uso scientifico dal valore di bilancio e dalla garanzia realizzabile.

**Flussi di cassa**: riconciliare saldo iniziale + incassi effettivi - pagamenti effettivi = saldo finale bancario, senza compensare con crediti di carbonio non venduti; esporre pagamenti a parti correlate, vincoli su cassa, disponibilità per obblighi ecologici, restricted grants.

## B. Valutazione (solo da perito indipendente)
1. Due diligence titoli e durata residua: un diritto a termine non ha valore terminale perpetuo di default.
2. Tre approcci: DCF su flussi disponibili, comparabili di **diritti giuridicamente comparabili**, costo/asset approach ove appropriato; indicare limiti e sensitività, mai comparare grant a equity value.
3. Scenari: nessun credito emesso, nessun compratore, 50% caduta prezzo, ritardo registrazione, reversal/incendio, revoca titolo, rischio correlato portafoglio e uscita non praticabile.
4. Rischio e tasso di sconto: valuta, giurisdizione, liquidità, durata, controparte, prezzo carbon, modello e governance; documentare fonti, metodologia, indipendenza e COI.
5. Report: data, firmatario, competenze, scopo, limiti di perizia, valore per intervallo, valore realizzabile separato, remediation, incertezze, dissent e assunzioni sensibili.

Non attribuire a PROMETHEUS i valori da case study Kwaxala (~US$13m, ~5%, ~7x) come parametri provati. Sono **claim esterni non convalidati contabile/contrattualmente**.

## C. Waterfall contrattuale candidato (non priorità legale già stabilita)
`EligibleCollectedCash = actual_bank_collections + cleared non-carbon contractual services` (grants vincolati tenuti separati). Sottrarre obblighi inderogabili, titolari dei diritti, tutela/minimo stewardship, costi di verifica, fondi reversal/incidenti, service operator fees approvate, debito e fiscalità **secondo il grado realmente applicabile**. Solo dopo ottenere `DistributableCash = MAX(0, cash_after_obligations)`. Contabilizzare `FundingGap = MAX(0,-cash_after_obligations)` **separatamente**. L'ordine economico desiderato non può derogare alla priorità di legge dei creditori.

Se `DistributableCash > 0`, dividere secondo una tabella di quote firmata e verificata, per esempio `community_contractual_share`, `investor_contractual_share`, `retained_reserve_share`, **senza inventare percentuali di Kwaxala né fissare alcun tasso promesso**. Se non esiste waterfall firmata: `ALLOCATION=UNDEFINED`, nessuna distribuzione ammessa.

## D. Registro distribuzioni e controlli
Schema CSV: `distribution_id, entity_id, holder_id_safe, claim_basis_contract_sha, period, accrued_entitlement, bank_cash_paid, carbon_serial_transferred, tax_withheld, reversal_adjustment, payment_date, bank_evidence_sha, unpaid_amount, independent_reviewer, status`. Qualunque blank è `UNKNOWN`, non pagamento zero. Scritture di `cash_paid` richiedono prova bancaria; crediti in natura richiedono titolarità, seriali, consegna, fiscale.

**Riconciliazioni:** `distributions <= distributable_cash` per specie di fondo e periodo salvo prove legali, `bank_paid=sum(transfers)`, `carbon sold cannot be used twice`, `ending_cash=opening_cash+inflows-outflows`; audita transazioni fra entità; conservare storici anche se negativi.

## E. Stress e rischio
Copertura mesi stewardship minimi, costo post-reversal, arretrati obbligatori, priorità creditori, rischio FX, cash trapped, quota locale dei flussi effettivamente documentati, correlation shock fra progetti. Aeterna/Ravel: distinguere rischio prevenuto, trasferito, trattenuto, residuo e portatore ultimo. Test con scenario cassa disponibile zero e creditori attivi.

## F. Allegato finanziario
`PRM_FINANCIAL_EVIDENCE_WATERFALL_TEMPLATE.xlsx` nel pacchetto: schede Readme, Assumptions, Waterfall, DistributionHistory, EvidenceGate. Gli eventuali numeri nel foglio scenario sintetico NON sono dati reali.

**Gate:** `SIGNED_FINANCIALS=UNKNOWN`, `INDEPENDENT_APPRAISAL=HOLD`, `REAL_DISTRIBUTION_HISTORY=NOT_PROVIDED`, `CAPITAL_READINESS=NO_GO`.

**Fonte case study:** https://www.ecosystemmarketplace.com/publications/gaining-ground-state-of-private-investment-in-nature-2026/kwaxala/ .


---
**v0.2 M2 derivative; predecessor:** 03_BILANCI_VALUTAZIONI_WATERFALL_DISTRIBUZIONI.md (historical v0.1 preserved unchanged). New annex is analytical and non-executable.

## M2 v0.2 — financial reconciliation and falsification tests
Never insert Kwaxala external publication figures as default PROMETHEUS underwriting assumptions. `~US$13m`, `US$1.8m placed`, `~7x` and `5% target` are externally reported examples; original signed balance sheets, subscription books, payments and note terms have not been reviewed.

**Three distinct value objects:** an ecology metric has no automatically recognized accounting value; a contractual right has fair value only if a qualified valuation methodology and evidence apply; collateral realizable value requires independent legal enforceability and liquidity analysis.

**Evidence workflow:** from sale/offset registry serial + buyer invoice + contract + cash bank receipt → bank reconciliation → restricted/usable cash → each legal stakeholder's contractual seniority → actual paid transfers. Distinguish site gross receipts, consolidated pooled receipts, grant funding, one-off philanthropy, restricted endowment and prospective fund commitments. Do not double-count the same carbon vintage as credits-in-kind AND cash sale.

**Waterfall check:** `Bank-cash-net-after-obligations = actual_eligible_receipts - actual_due_and_paid_costs - reserved_amounts`; `Distributable=max(0,net)`; `Shortfall=max(0,-net)`. When rights/payment priority documents are absent, disable the allocation algorithm (`HOLD`), not simply present a preferred share of 90%. Always label `HYPOTHETICAL`, `REAL_VERIFIED`, or `UNKNOWN` by cell.

**Minimum independent financial evidence:** accounting period/currency; auditor scope/COI; balance sheet, income and cash flow; notes on intangible rights and impairments; valuation appraisal (case/scope/marketability), restricted grants, issued/unissued credits by vintage, signed paid entitlement ledger, claims on assets and insolvency recovery expectations.

**Stress tests:** zero issued carbon; carbon -50% and -100% price; 2y issuance delay; currency mismatch; reversal and remediation obligations; loss of legal tenure; default of buyer or fund; negative annual net cash; simultaneous multiple site drawdowns. State unhedged ultimate risk bearer.
