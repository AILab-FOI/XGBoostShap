# Metodologija čišćenja i predobrade podataka

Ovaj dokument opisuje implementirane strategije za rukovanje nedostajućim vrijednostima i tretman ekstrema (outliera) u financijskom datasetu. Cilj je maksimizirati kvalitetu ulaznih podataka za XGBoost model, uz minimiziranje gubitka informacija i uvođenja biasa.

## 1. Napredna imputacija (MICE)
Za razliku od standardnih pristupa (popunjavanje srednjom vrijednosti ili medijanom), koji često iskrivljuju varijancu i "spljošte" distribuciju, implementiran je **MICE (Multivariate Imputation by Chained Equations)** algoritam.

*   **Racionala:** Financijski podaci su visoko korelirani (npr. *prihod* i *iznos kredita* su često povezani). Obična imputacija ignorira te veze.
*   **Implementacija:**
    *   Svaka varijabla s nedostajućim podacima tretira se kao ciljna varijabla u regresijskom modelu, dok ostale varijable služe kao prediktori.
    *   Proces je iterativan (ciklira se kroz značajke) dok se procjene ne stabiliziraju.
    *   Ovaj pristup čuva multivarijatne odnose u podacima, što je ključno za kasnije modeliranje interakcija u XGBoostu.

## 2. Detekcija i tretman outliera
S obzirom na to da radimo s podacima o kreditnom riziku, "outlier" nije uvijek greška – često predstavlja klijenta visokog rizika. Zato je pristup konzervativan kako ne bismo uklonili validne signale za *default*.

Korišten je hibridni pristup:

### A. Statistički pristup: IQR (Interquartile Range)
Za univarijatnu analizu koristimo robusnu statistiku otpornu na ekstreme.
*   Definiramo granice kao $Q1 - 1.5 \times IQR$ i $Q3 + 1.5 \times IQR$.
*   **Tretman:** Umjesto brisanja redaka (dropping), primjenjuje se **Winsorization (capping)**. Vrijednosti izvan granica se "režu" i postavljaju na gornju/donju granicu (npr. 5. i 95. percentil). Time zadržavamo klijenta u datasetu, ali smanjujemo utjecaj ekstrema na skaliranje.

### B. Algoritamski pristup: Isolation Forest
Za detekciju multivarijatnih anomalija (npr. klijent s niskim prihodima, ali ogromnim limitom kartice – kombinacija koja je sumnjiva, iako su pojedinačne vrijednosti možda unutar granica).
*   Koristi se *Isolation Forest* algoritam koji izolira točke nasumičnim grananjem stabla.
*   Anomalije se izoliraju brže (imaju kraći put u stablu).
*   Ovi zapisi se ne brišu automatski, već se označavaju (flagging) novom binarnom varijablom `is_anomaly`, dopuštajući modelu da sam nauči nosi li ta anomalija informaciju o riziku.
