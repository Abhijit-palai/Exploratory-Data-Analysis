#Use pairplot/correlation matrix for feature relationships

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("Titanic-Dataset.csv")  # Replace with your file path

# Select only numeric columns
numeric_df = df.select_dtypes(include='number')

# 1. Pairplot (scatterplot matrix)
sns.pairplot(numeric_df)
plt.suptitle("Pairplot of Numeric Features", y=1.02)
plt.show()

# 2. Correlation Matrix with Heatmap
corr = numeric_df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', square=True, linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()
