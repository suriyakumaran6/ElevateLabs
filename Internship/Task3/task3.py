import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame

print(df.info())
print(df.head())

num_cols = df.columns[:-1]

df[num_cols].hist(figsize=(10, 8))
plt.suptitle("Distribution of Numerical Features")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x=df['target'])
plt.title("Count of Each Iris Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10,6))
df[num_cols].boxplot()
plt.title("Box Plot for Outlier Detection")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,6))
corr = df[num_cols].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

feature_corr = df.corr()['target'].sort_values(ascending=False)
print(feature_corr)

print("""
1. Petal length and petal width show strong correlation with species.
2. Sepal features show weaker correlation.
3. No extreme outliers detected.
4. Dataset is well balanced.
5. Petal length and petal width are most important for prediction.
""")
