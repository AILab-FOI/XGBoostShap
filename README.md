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
- [ ] **napredna eda i statistika:**
    - [ ] vizualizacija distribucija (histogrami, boxplotovi).
    - [ ] statistički testovi normalnosti (shapiro-wilk / kolmogorov-smirnov).
    - [ ] analiza korelacija (pearson za linearne, spearman za nelinearne odnose).
    - [ ] detekcija multikolinearnosti (vif - variance inflation factor).

### faza 2: feature engineering i predobrada (tjedan 4-6)
- [ ] **pipeline za čišćenje:**
    - [ ] napredna imputacija (mice - multivariate imputation) umjesto običnog prosjeka.
    - [ ] tretman outliera (iqr metoda ili isolation forest).
- [ ] **konstrukcija značajki (domain knowledge):**
    - [ ] kreiranje financijskih omjera (npr. debt-to-income, utilization rate).
    - [ ] binning kontinuiranih varijabli (weight of evidence - woe transformacija).
    - [ ] interakcijske značajke (polinomske kombinacije ključnih varijabli).
- [ ] **selekcija značajki:**
    - [ ] filtriranje pomoću `boruta` algoritma ili recursive feature elimination (rfe).
    - [ ] dokumentiranje zadržanih vs. odbačenih varijabli.

### faza 3: modeliranje i rigorozna validacija (tjedan 7-10)
- [ ] **baseline modeli:**
    - [ ] logistička regresija (za usporedbu linearnosti).
    - [ ] random forest (kao jednostavniji ensemble benchmark).
- [ ] **razvoj xgboost modela:**
    - [ ] implementacija custom loss funkcije (ako je potrebno zbog cijene pogreške).
    - [ ] postavljanje `scale_pos_weight` za rješavanje nebalansiranih klasa.
- [ ] **napredna optimizacija (bayesian):**
    - [ ] implementacija `optuna` studije za hiperparametre.
    - [ ] vizualizacija hiperparametarskog prostora (slice plots).
- [ ] **znanstvena validacija (gold standard):**
    - [ ] implementacija **nested cross-validation** (5x2 ili 10x5) za realnu procjenu greške.
    - [ ] analiza krivulja učenja (learning curves) za dijagnozu bias/variance trade-offa.
    - [ ] threshold tuning: optimizacija praga odluke za maksimizaciju f1-scorea ili profita.

### faza 4: explainable ai (xai) i fairness (tjedan 11-13)
- [ ] **shap analiza (model agnostic):**
    - [ ] beeswarm plotovi za globalni feature importance.
    - [ ] dependence plotovi za analizu nelinearnosti.
    - [ ] interakcijske matrice.
- [ ] **usporedba metoda:**
    - [ ] usporedba shap rezultata s permutation importance metodom.
- [ ] **fairness i bias analiza:**
    - [ ] provjera pristranosti modela prema osjetljivim grupama (npr. dob, spol - ako postoje u podacima).
    - [ ] izračun metrika: disparate impact ratio, equal opportunity difference.

### faza 5: inženjering, reproducibilnost i izvještaj (tjedan 14-15)
- [ ] **kvaliteta koda:**
    - [ ] type hinting (mypy) i formatiranje (black/flake8).
    - [ ] pisanje unit testova (`pytest`) za ključne funkcije pipelinea.
- [ ] **reproducibilnost:**
    - [ ] kreiranje `dockerfile` za izolaciju okruženja.
    - [ ] postavljanje `reproducibility_guide.md`.
- [ ] **finalni deliverables:**
    - [ ] pisanje znanstvenog izvještaja u latex formatu (struktura: abstract, method, results, discussion).
    - [ ] generiranje finalnih vizualizacija visoke rezolucije.
    - [ ] snimanje kratkog demo videa ili gif-a za readme.
