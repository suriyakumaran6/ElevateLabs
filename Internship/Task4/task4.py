import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

df = pd.read_csv("adult.csv")

print("\n--- Initial Dataset Info ---")
print(df.info())

print("\n--- First 5 Rows ---")
print(df.head())

categorical_cols = df.select_dtypes(include=['object']).columns
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

print("\nCategorical Columns:", list(categorical_cols))
print("Numerical Columns:", list(numerical_cols))

label_cols = ['income'] if 'income' in df.columns else []

le = LabelEncoder()
for col in label_cols:
    df[col] = le.fit_transform(df[col])

one_hot_cols = list(set(categorical_cols) - set(label_cols))
df = pd.get_dummies(df, columns=one_hot_cols, drop_first=True)

print("\n--- Dataset After Encoding ---")
print(df.head())

scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

print("\n--- Dataset After Scaling ---")
print(df.head())

print("\n--- Final Dataset Info ---")
print(df.info())

df.to_csv("adult_preprocessed.csv", index=False)
print("\nPreprocessed dataset saved as 'adult_preprocessed.csv'")
