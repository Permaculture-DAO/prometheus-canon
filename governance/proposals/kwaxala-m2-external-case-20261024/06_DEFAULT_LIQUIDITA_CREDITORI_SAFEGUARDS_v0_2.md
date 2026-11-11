---
document_id: PRM-KWX-EXT-CASE-G06@0.2-CANDIDATE
status: RISK_AND_INSOLVENCY_TERM_SHEET_NON_EXECUTABLE
source_authority: NONE
---
# FASCICOLO 06 — Default, liquidità, durata, riscatti, creditori, comunità, conflitti
**Scopo:** principi per uno studio contrattuale da sottoporre a legali per ciascuna giurisdizione, attuario e custode. Non sono condizioni valide già approvate né garanzie agli investitori. La **priorità legale dei creditori** e l'efficacia delle tutele comunitarie non possono essere inventate o sovrascritte da un algoritmo.

## A. Term sheet non vincolante
| Tema | Schema di tutela / rischio | Prova/decisione necessaria |
|---|---|---|
| Durata | Titoli forestali, licenze, stewardship, crediti e partecipazioni hanno scadenze distinte | title register + counsel |
| Event of default | non-payment, titolo nullo, frode, dati falsi, violazioni ambientali, insolvency, consenso revocato ove legalmente applicabile | definizione e rimedi con counsel |
| Liquidity | assumere illiquidità e impossibilità di uscita fino a prova opposta | condizioni di mercato e diritto di trasferimento |
| Redemption | sospensione/riscatto solo se previsto e lecito, non promessa implicita | capital liquidity plan |
| Ranking | creditori garantiti/non garantiti/enti pubblici secondo legge, non secondo preferenze etiche | insolvency counsel |
| Cross-default | impedire contagio fra siti se legalmente/contrattualmente realizzabile | review cross-collateral |
| Stewardship | riservare poteri ambientali locali senza illusione di immunità a esecuzione | territorial counsel |
| Reversal | obblighi ambiente/carbon e finanziamento della permanenza | method + reserve |
| Governance | related-party disclosure, reviewer indipendenti, meccanismi reclamo e whistleblowing | minutes+COI ledger |
| Transfer of shares | restrizioni normative, controlli dei beneficiari e investor protection | securities counsel |

## B. Clausole concettuali, NON legalmente efficaci
**Protezione comunitaria:** nessun evento relativo a un mero finanziatore attribuisce automaticamente poteri di alienazione, taglio o gestione del bosco a quel finanziatore. La disposizione deve essere convertita in un patto **opponibile**, se consentito, su titoli effettivi.

**Trasparenza del rendimento:** nessuna garanzia di yield fisso/perpetuo; tutte le distribuzioni derivano da cassa utilizzabile, priorità e riserve realmente previste. Il rischio di perdita totale e mancata liquidità può sussistere.

**Separazione entità:** conti, servizi e garanzie differenziati; una SPV non crea automaticamente bankruptcy remoteness e non sostituisce i pareri sulla responsabilità dei soggetti.

**Incident stop:** in caso di illegalità del titolo, conflitto consenso, perdita irreversibile forestale, reversal non coperto o sospetto seriale duplicato, stop di nuove attestazioni/digital-rights e finanza finché non interviene decisore competente. Permangono obblighi inderogabili e servizi di protezione.

## C. Ravel Risk Register obbligatorio
`risk_id, hazard, trigger, exposed_party, vulnerability, direct_loss, secondary_loss, frequency_basis, severity_range, scenario_dependence, mitigation, retained_loss, transferred_loss, residual_loss, ultimate_bearer, legal_evidence, confidence, gate`.

**Stress da simulare:** (1) 0 crediti nuovi per tre stagioni; (2) 50% prezzo e quota invenduta; (3) incendio regionale e fallimento correlato più siti; (4) revoca titoli o ABAs; (5) insolvency provider; (6) insolvency fondo; (7) contenzioso sui diritti; (8) caduta revisore/registri e perdita dei dati; (9) mutamento legislativo sulla classificazione security; (10) scissione dei partner comunitari. Per ogni stress calcolare almeno perdita, gap minimo stewardship, cash coverage, chi paga e chi sopporta danno se non paga nessuno.

**Invarianti:** `LOSS_REDUCTION != LOSS_ALLOCATION`, `TRANSFERRED_RISK != ELIMINATED_RISK`, `UNKNOWN != ZERO`, `asset appraisal != liquid collateral`, `insured != insurance bound`, `token != enforceable right`.

## D. Conflitti di interesse: registro
Identità della controparte e del beneficiario effettivo, relazione con manager/investitore/ONG/verificatore, fee totale, alternative comparabili, delibera e astensione quando prevista, disponibilità del documento, impatti sulla comunità, ricorsi e criterio di rinnovo. Nessun revisore retribuito esclusivamente per risultati positivi.

## E. Giurisdizioni e autorizzazioni
- **BC/Canada:** tenure Crown, stewardship della First Nation, diritti atmosferici/ABA, insolvency e norme su securities da validare sullo specifico veicolo e offerta.
- **USA/Florida:** qualificazione security/investment contract, collocamento, emissione e transazioni; una LLC non esenta dai requisiti federali.
- **Italia/UE:** MiFID II/AIFMD, ESMA/MiCA nei limiti pertinenti, obblighi offerta, antiriciclaggio, imposte, forest/cadastral laws; nessuna deduzione che l'emissione di token implichi una licenza.

**Decisione:** `CONTRACT_DRAFT_RESEARCH=GO`; `ISSUANCE_OR_PUBLIC_OFFER=NO_GO`; `LEGAL_ENFORCEABILITY=HOLD`; `DEFAULT_PROTECTION_PROVEN=NO`; `RAVEL=SHADOW_ONLY`.

**Fonti:** https://www.sec.gov/newsroom/speeches-statements/corp-fin-statement-tokenized-securities-012826-statement-tokenized-securities ; https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/transactions-involving-crypto-assets ; https://www.esma.europa.eu/esmas-activities/investors-and-issuers/fund-management ; https://www.esma.europa.eu/document/guidelines-conditions-and-criteria-qualification-crypto-assets-financial-instruments .


---
**v0.2 M2 derivative; predecessor:** 06_DEFAULT_LIQUIDITA_CREDITORI_SAFEGUARDS.md (historical v0.1 preserved unchanged). New annex is analytical and non-executable.

## M2 v0.2 — adverse-case contractual simulations and actual bearer
The public motto that investments remain passive and forest control local must be enforceably stress-tested under mandatory insolvency, lien, security and creditor priority rules; a proposed moral obligation is not sufficient.

For each scenario allocate `Loss_Exposure_ID`, currency, date and probability range (if defensible), primary contractual obligor, guarantee/recourse, rights-holder, collateral description, reserve, transfer to third party and residual bearer. Unknown bearer must be a stop condition for capital/issuer readiness, not assumed borne by a hypothetical diversified fund.

**Cases**: zero carbon issuance; carbon sale agreed but credits cancelled; regulator refuses offsets; major natural reversal; annual stewardship funding gap; fund insolvency and central-service outage; recourse to Nation; creditor foreclosure over rights; legal challenge over ABA; conflict with Indigenous free/prior informed consent where applicable; currency devaluation; merger/transfer to unrelated owner; perpetuity claim with fixed-term tenure.

**Separate legal priorities** (mandatory) from *preferred distribution policy* (discretionary). Never state cash reserves are legally segregated unless trustee/account/contract proof exists. The operator agreement must provide a remedy for data custody and continuous ecology monitoring on intermediary failure, subject to local law/authority. Contractual consent, rights and disclosures reviewed by qualified counsel.

**Audit result rule:** No qualified contract set ⇒ `ULTIMATE_LOSS_BEARER=UNKNOWN`, `UNDEWRITING_READINESS=HOLD`; no insurance, risk annihilation, 5% promise or transferable risk designation.
