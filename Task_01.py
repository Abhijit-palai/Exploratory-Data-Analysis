#Generate summary statistics (mean, median, std, etc.).

import pandas as pd
import numpy as np

# Load the file (update 'your_file.csv' to your file path)
df = pd.read_csv("Titanic-Dataset.csv")  

print(df.head())

# Summary statistics
summary = df.describe(include='all')  # Include='all' includes categorical and numeric
print("Summary statistics:\n", summary)


for col in df.select_dtypes(include=np.number).columns:
    print(f"\nColumn: {col}")
    print(f"Mean: {df[col].mean()}")
    print(f"Median: {df[col].median()}")
    print(f"Standard Deviation: {df[col].std()}")
    print(f"Variance: {df[col].var()}")
    print(f"Min: {df[col].min()}")
    print(f"Max: {df[col].max()}")
