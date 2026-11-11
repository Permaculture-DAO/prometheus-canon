---
document_id: PRM-KWX-EXT-CASE-G05@0.2-CANDIDATE
status: FALSIFIABLE_RESEARCH_HYPOTHESIS_NOT_CENTREE
source_authority: NONE
---
# FASCICOLO 05 — Matematica ecologica, dati, incertezza, test predittivi
**Avvertenza:** formule originali di Centree, dataset validati, coefficienti e protocollo integrale non risultano disponibili in questo audit. Questa è un'**alternativa originale di ricerca PROMETHEUS** (`Forest Ecological Function Vector — FEFV@0.1`), non un reverse engineering, non un Centree Token, non tCO2e certificati né un prodotto finanziario.

## A. Oggetto e grafo relazionale
`ForestSite {site_id, geometry_sha, ecoregion, tenure_id, consent, management_ledger, baseline_date, protection_date, site_strata[], review}`. Ogni relazione ecologica: `subject_taxon/or abiotic`, `object`, `interaction_type` (competizione/facilitazione/allelochimica/predazione/idrologia), segno **contestuale**, direzione, finestra temporale, unità, esposizione, meccanismo alternativo, evidenza esperimento, grado trasferibilità, fonte+hash. Una co-occorrenza non prova causalità.

## B. Vettore osservabile prima dello score
Per sito `s`, periodo `t` e campionamento indipendente `p` definire un vettore non monetario:
`X(s,t) = [H, B, S, W, C, R]` con:
- H: eterogeneità struttura forestale, livelli, classi età/diametro, deadwood e alberi vetusti osservati;
- B: biodiversità nativa e guild funzionali, effort, specie introdotte/invasive, rischio di estinzione locale;
- S: stabilità/infiltrazione del suolo, SOC verificato, struttura e densità apparente;
- W: acqua nel suolo, infiltrazione, qualità, deflussi, siccità, evapotranspirazione a bilancio;
- C: stock e flussi carbonio **fisici** con incertezza, non seriali creditabili;
- R: recupero post-disturbo, resistenza, condizioni di permanenza, dipendenza da interventi.
Il diritto locale, la qualità delle prove e il consenso sono `GATES` separati e **non migliorano artificialmente le misure biofisiche**. Ogni dimensione ha propri endpoint e unità.

## C. Specifica matematica candidata
Per una metrica orientata al beneficio `x_j`, soltanto se soglie esterne `L_j,U_j` pre-registrate con `U_j>L_j`, è ammessa la visualizzazione normalizzata
`z_j = min(1,max(0,(x_j-L_j)/(U_j-L_j)))`.
Per indicatori di danno, invertire il verso e dichiarare la funzione. Registrare limiti di saturazione, outlier e raw values: `z_j=0` non significa ecosistema privo di funzione.

Per prima release **non usare score unico**. Solo in studio separato, opzionale: `I=SUM(w_j*z_j)` con `w_j>=0`, `SUM(w_j)=1`, pesi congelati esternamente; testare ranking con pertubazione dei pesi, non compensabilità di perdite ecologiche critiche e conflitti normativi. Nessun valore `I` è convertibile in proprietà, credito o token. Metriche mancanti => `UNASSESSABLE`, non zero e non media imputata.

L'incertezza di ogni metrica deriva da campioni realmente indipendenti, precisione strumenti, incertezza del modello e eterogeneità sito. Metodo: intervalli bootstrap **per blocchi/siti**, modello gerarchico appropriato o Monte Carlo con correlazioni, dopo piano statistico congelato. Serie temporali dense dello stesso sensore non equivalgono a 1000 siti biologicamente indipendenti.

## D. Protocolli esperimenti e falsificazione
- **H-E1 predizione**: FEFV migliora la predizione out-of-sample di sopravvivenza specie native, recupero idrologico o funzionalità ecologica rispetto a baseline semplice NDVI/canopy/età forestale o esperto + GIS. **Falsificata** se incremento non è praticamente significativo o costo/fragilità maggiore.
- **H-E2 causalità**: gestione rigenerativa modifica endpoint ecologici rispetto a comparatori adeguati, correggendo climate, suolo e storia. Se confondimento/sovrapposizione non separabile, classificare `ASSOCIATION_ONLY`.
- **H-E3 maturità**: le metriche di struttura di boschi maturi predicono specifici habitat/service outcomes in più ecoregioni. Falsificata da generalizzazione inversa o domain-shift incontrollato.
- **H-E4 biomimetica organiz.** Il lifecycle Placenta→Climax produce decisioni migliori di un workflow semplice, con costo/errore/indipendenza verificati; si semplifica se aggiunge complessità senza beneficio.

**Pre-registrazione:** campione, unità sperimentale, gruppo di confronto, endpoint primario, disturbo definito, varianza locale, MDE, potenza, analisi errori, cutoffs, licenze, reviewer indipendente e regola di arresto prima di osservare gli esiti. Blind evaluator se possibile. Tenere negativo/null/avverso come risultato primario.

## E. Data dictionary per Evidence Spine
`observation_id, plot_id, site_id, stratum, polygon_hash, timestamp, metric, value, unit, method_sha, raw_data_sha, reviewer_id, instrument, calibration_sha, spatial_resolution, uncertainty, missingness, consent_class, data_license, QA_state`. Niente estrazione di conoscenze indigene tradizionali o località sensibili senza consenso esplicito.

## F. Modulo CEREBRO non duplicativo
CEREBRO: catalogo ipotesi fonti e validità; Atlas/Bridge: geometrie; Evidence Spine: osservazioni; REI: valore condizionato a diritti, non mapping di indice; Aeterna/Ravel: rischi e perdite. Il documento `PRM_SYNTROPIC_PLACENTA_CLIMAX_RENEWAL_KNOWLEDGE_SOURCE_v1_0_CANDIDATE` resta fonte candidata di analogia organizzativa, non algoritmo naturalistico deterministico.

**Test sintetici di errore:** denominatore 0, unità incompatibili, orientamento invertito, missing data, pseudo-replication, species bias, sensor drift, geofence overlap, positive leakage, false carbon-equivalence. Bloccare `ECOLOGICAL_CERTIFICATION` in tutte queste condizioni.

**Fonti:** https://www.centree.org/ ; https://www.kwaxala.com/ ; https://doi.org/10.1016/S2542-5196(25)00047-6 ; https://doi.org/10.1016/j.lanplh.2025.101312 .


---
**v0.2 M2 derivative; predecessor:** 05_CENTREE_ALTERNATIVE_FALSIFIABLE_ECOLOGY.md (historical v0.1 preserved unchanged). New annex is analytical and non-executable.

## M2 v0.2 — ecologically falsifiable alternative, not Centree reverse engineering
The existing PROMETHEUS multi-dimensional proposal must not be described as an authorized Centree implementation. The proprietary Centree computation, if any, is unavailable in full replicable public form. This M2 **research alternative** generates provisional outcomes, never a unit of carbon, security or financial right.

**Uncertainty disclosure:** each indicator has spatial support, observation/model provenance, instrument errors, seasonal range, laboratory QA, observer inter-rater reliability, missingness, non-stationarity and confidence/prediction interval. `UNKNOWN` never becomes zero. A "forest age" index must be tested outside its training ecosystem and not extrapolated to Mediterranean agroforestry/Genesis without domain-shift analysis.

**Preregister two distinct studies:** `ECO-BIOL` forest native composition/structural/soil and hydrological outcomes; `ECO-PRED` whether an augmented maturity feature vector improves *out-of-sample* predictive accuracy over the cheapest strong comparator (e.g. NDVI+age+GIS+expert), with a separately specified minimum practically meaningful gain and documented total system cost. Spatially block folds so adjacent sites don't leak into test sets.

**Negative result receipt:** when higher complexity does not beat simple ecological assessment, **RETIRE/SIMPLIFY** the extra model. Field claims and corporate analogy must remain separate. The Placenta→Climax stage is an organizational hypothesis that requires independent outcomes; it is not itself a forest age classifier.

**Community data governance:** obtain authority to process knowledge and ecological sensitivities; preserve access restrictions; do not publish exact sensitive species/local sacred site coordinates or culturally proprietary data merely because recorded on DHT.
