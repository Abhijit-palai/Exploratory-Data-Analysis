#Identify patterns, trends, or anomalies in the data.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data
df = pd.read_csv("Titanic-Dataset.csv")  


print("Shape of Data:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)
print("\nSummary Statistics:\n", df.describe(include='all'))

# 2. Distribution of numeric features
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols].hist(bins=30, figsize=(15, 10), layout=(len(numeric_cols) // 3 + 1, 3))
plt.suptitle("Distribution of Numeric Features")
plt.tight_layout()
plt.show()

# 3. Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df[numeric_cols].corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# 4. Boxplots for Outlier Detection
for col in numeric_cols:
    plt.figure(figsize=(6, 3))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()

# 5. Optional: Pairplot
sns.pairplot(df[numeric_cols])
plt.suptitle("Pairplot of Numeric Features", y=1.02)
plt.show()
