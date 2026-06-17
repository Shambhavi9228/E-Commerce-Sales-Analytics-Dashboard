import pandas as pd

# Load dataset
df = pd.read_csv("../data/Sample - Superstore.csv", encoding="latin1")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# Convert Order Date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Save cleaned data
df.to_csv("../data/cleaned_superstore.csv", index=False)

print("\nCleaned dataset saved successfully!")