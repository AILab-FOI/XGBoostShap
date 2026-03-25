## plan istraživanja i razvoja (roadmap)
"Probabilistic Assessment of Financial Default Risk via Bayesian-Optimized Gradient Boosting and Game-Theoretic Feature Attribution"
ovaj repozitorij prati 15-tjedni istraživački projekt s ciljem razvoja, optimizacije i interpretacije robustnog sustava za procjenu financijskog rizika. fokus je na znanstvenoj metodologiji i inženjerskoj reproducibilnosti.

### faza 1: postavljanje, podaci i statistička analiza (tjedan 1-3)
- [x] **infrastruktura:**
    - [x] inicijalizacija gita i .gitignore (python/pycharm).
    - [x] postavljanje `dvc` (data version control) za praćenje verzija dataseta.
    - [] konfiguracija virtualnog okruženja (`poetry` ili `venv`).
- [x] **akvizicija i validacija podataka:**
    - [x] odabir high-dimensional financijskog dataseta (npr. german credit data ili taiwan bankruptcy).
    - [x] provjera integriteta podataka i detekcija duplikata.
- [x] **napredna eda i statistika:**
    - [x] vizualizacija distribucija (histogrami, boxplotovi).
    - [x] statistički testovi normalnosti (shapiro-wilk / kolmogorov-smirnov).
    - [x] analiza korelacija (pearson za linearne, spearman za nelinearne odnose).
    - [x] detekcija multikolinearnosti (vif - variance inflation factor).

### faza 2: feature engineering i predobrada (tjedan 4-6)
- [x] **pipeline za čišćenje:**
    - [x] napredna imputacija (mice - multivariate imputation) umjesto običnog prosjeka.
    - [x] tretman outliera (iqr metoda ili isolation forest).
- [x] **konstrukcija značajki (domain knowledge):**
    - [x] kreiranje financijskih omjera (npr. debt-to-income, utilization rate).
    - [x] binning kontinuiranih varijabli (weight of evidence - woe transformacija).
    - [x] interakcijske značajke (polinomske kombinacije ključnih varijabli).
- [x] **selekcija značajki:**
    - [x] filtriranje pomoću `boruta` algoritma ili recursive feature elimination (rfe).
    - [x] dokumentiranje zadržanih vs. odbačenih varijabli.

### faza 3: modeliranje i rigorozna validacija (tjedan 7-10)
- [x] **baseline modeli:**
    - [x] logistička regresija (za usporedbu linearnosti).
    - [x] random forest (kao jednostavniji ensemble benchmark).
- [x] **razvoj xgboost modela:**
    - [x] implementacija custom loss funkcije (ako je potrebno zbog cijene pogreške).
    - [x] postavljanje `scale_pos_weight` za rješavanje nebalansiranih klasa.
- [x] **napredna optimizacija (bayesian):**
    - [x] implementacija `optuna` studije za hiperparametre.
    - [x] vizualizacija hiperparametarskog prostora (slice plots).
- [x] **znanstvena validacija (gold standard):**
    - [x] implementacija **nested cross-validation** (5x2 ili 10x5) za realnu procjenu greške.
    - [x] analiza krivulja učenja (learning curves) za dijagnozu bias/variance trade-offa.
    - [x] threshold tuning: optimizacija praga odluke za maksimizaciju f1-scorea ili profita.

### faza 4: explainable ai (xai) i fairness (tjedan 11-13)
- [x] **shap analiza (model agnostic):**
    - [x] beeswarm plotovi za globalni feature importance.
    - [x] dependence plotovi za analizu nelinearnosti.
    - [x] interakcijske matrice.
- [x] **usporedba metoda:**
    - [x] usporedba shap rezultata s permutation importance metodom.
- [x] **fairness i bias analiza:**
    - [x] provjera pristranosti modela prema osjetljivim grupama (npr. dob, spol - ako postoje u podacima).
    - [x] izračun metrika: disparate impact ratio, equal opportunity difference.

### faza 5: inženjering, reproducibilnost i izvještaj (tjedan 14-15)
- [x] **kvaliteta koda:**
    - [x] type hinting (mypy) i formatiranje (black/flake8).
    - [x] pisanje unit testova (`pytest`) za ključne funkcije pipelinea.
- [x] **reproducibilnost:**
    - [x] kreiranje `dockerfile` za izolaciju okruženja.
    - [x] postavljanje `reproducibility_guide.md`.
- [ ] **finalni deliverables:**
    - [ ] pisanje znanstvenog izvještaja u latex formatu (struktura: abstract, method, results, discussion).
    - [x] generiranje finalnih vizualizacija visoke rezolucije.
    - [ ] snimanje kratkog demo videa ili gif-a za readme.
