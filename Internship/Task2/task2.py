import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("house-prices.csv")
print("\n--- Initial Dataset Info ---")
print(df.info())
df_before = df.copy()
print("\n--- Missing Values Count ---")
missing_values = df.isnull().sum()
print(missing_values)
missing_values = missing_values[missing_values > 0]

if not missing_values.empty:
    missing_values.plot(kind='bar', figsize=(10,5))
    plt.title("Missing Values per Column")
    plt.xlabel("Columns")
    plt.ylabel("Missing Count")
    plt.tight_layout()
    plt.show()
else:
    print("No missing values to visualize.")

missing_percent = df.isnull().mean() * 100
cols_to_drop = missing_percent[missing_percent > 40].index

print("\nDropping columns with >40% missing values:")
print(list(cols_to_drop))

df.drop(columns=cols_to_drop, inplace=True)

num_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

cat_cols = df.select_dtypes(include=['object']).columns

for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\n--- Missing Values After Cleaning ---")
print(df.isnull().sum())

print("\n--- Cleaned Dataset Info ---")
print(df.info())

print("\n--- Dataset Comparison ---")
print("Before Cleaning Shape:", df_before.shape)
print("After Cleaning Shape :", df.shape)

df.to_csv("cleaned_dataset.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_dataset.csv'")
