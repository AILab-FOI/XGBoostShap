import pandas as pd
import numpy as np

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.linear_model import BayesianRidge
from sklearn.ensemble import IsolationForest

imputer = IterativeImputer(
    estimator=BayesianRidge(),
    max_iter=10,
    random_state=42
)

df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

for col in df_imputed.select_dtypes(include=np.number).columns:
    q1 = df_imputed[col].quantile(0.05)
    q3 = df_imputed[col].quantile(0.95)
    df_imputed[col] = df_imputed[col].clip(lower=q1, upper=q3)

iso_forest = IsolationForest(
    n_estimators=200,
    contamination=0.05,
    random_state=42
)

df_imputed["is_anomaly"] = (iso_forest.fit_predict(df_imputed.select_dtypes(include=np.number)) == -1).astype(int)
