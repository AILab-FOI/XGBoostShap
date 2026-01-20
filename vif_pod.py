import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

data = {
    'varijabla_1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'varijabla_2': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 
    'varijabla_3': [1, 1, 2, 3, 5, 8, 13, 21, 34, 55],
    'varijabla_4': [10, 9, 2, 3, 5, 1, 4, 6, 2, 1]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.heatmap(df.corr(method='pearson'), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Pearsonova korelacija")

plt.subplot(1, 2, 2)
sns.heatmap(df.corr(method='spearman'), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Spearmanova korelacija")
plt.tight_layout()
plt.show()

X = add_constant(df)
vif_data = pd.DataFrame()
vif_data["Varijabla"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print(vif_data)
