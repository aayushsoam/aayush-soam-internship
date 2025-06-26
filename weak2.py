import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

# Ensure folder for plots
os.makedirs("plots", exist_ok=True)

# Load cleaned data
df = pd.read_csv("cleaned_ghg_data.csv")

# Drop extra column if exists
if 'Unnamed: 7' in df.columns:
    df.drop(columns=['Unnamed: 7'], inplace=True)

# ------------------ Encode Categorical Columns ------------------
substance_map = {'carbon dioxide': 0, 'methane': 1, 'nitrous oxide': 2, 'other GHGs': 3}
df['Substance'] = df['Substance'].map(substance_map)

unit_map = {'kg/2018 USD, purchaser price': 0, 'kg CO2e/2018 USD, purchaser price': 1}
df['Unit'] = df['Unit'].map(unit_map)

source_map = {'Commodity': 0, 'Industry': 1}
df['Source'] = df['Source'].map(source_map)

# ------------------ Overview ------------------
print("\n Dataset Info:")
print(df.info())

print("\n Null Values:")
print(df.isnull().sum())

print("\n Summary Stats:")
print(df.describe().T)

# ------------------ Target Variable Distribution ------------------
plt.figure(figsize=(6, 5))
sns.histplot(df['Supply Chain Emission Factors with Margins'], bins=50, kde=True)
plt.title('Target Variable Distribution')
plt.xlabel('Supply Chain Emission Factors with Margins')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("plots/target_distribution.png")
plt.show()

# ------------------ Top 10 Emitting Industries ------------------
top_emitters = df[['Name', 'Supply Chain Emission Factors with Margins']] \
    .groupby('Name') \
    .mean() \
    .sort_values('Supply Chain Emission Factors with Margins', ascending=False) \
    .head(10).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(
    x='Supply Chain Emission Factors with Margins',
    y='Name',
    data=top_emitters,
    palette='viridis'
)

for i, (value, _) in enumerate(zip(top_emitters['Supply Chain Emission Factors with Margins'], top_emitters['Name']), start=1):
    plt.text(value + 0.01, i - 1, f'#{i}', va='center', fontsize=11, fontweight='bold', color='black')

plt.title('Top 10 Emitting Industries', fontsize=14, fontweight='bold')
plt.xlabel('Emission Factor (kg CO2e/unit)')
plt.ylabel('Industry')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("plots/top_10_emitting_industries.png")
plt.show()

# ------------------ Drop Unwanted Columns ------------------
df.drop(columns=['Name', 'Code', 'Year'], inplace=True)

# ------------------ Feature-Target Split ------------------
X = df.drop(columns=['Supply Chain Emission Factors with Margins'])
y = df['Supply Chain Emission Factors with Margins']

print("\n Feature shape:", X.shape)
print("\n Target Preview:")
print(y.head())

# ------------------ Univariate Count Plot: Substance ------------------
plt.figure(figsize=(6, 3))
sns.countplot(x=X['Substance'])
plt.title("Count Plot: Substance")
plt.xlabel("Substance")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("plots/substance_countplot.png")
plt.show()

# ------------------ Univariate Count Plot: Unit ------------------
plt.figure(figsize=(6, 3))
sns.countplot(x=X['Unit'])
plt.title("Count Plot: Unit")
plt.xlabel("Unit")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("plots/unit_countplot.png")
plt.show()
# ------------------ Univariate Count Plot: Source ------------------
plt.figure(figsize=(6, 4))
sns.countplot(x=X['Source'])
plt.title("Count Plot: Source (Industry vs Commodity)")
plt.xlabel("Source")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("plots/source_countplot.png")
plt.show()
# ------------------ Multivariate Analysis: Correlation Heatmap ------------------
plt.figure(figsize=(12, 8))

# Compute correlation matrix for numerical columns only
correlation_matrix = df.select_dtypes(include=np.number).corr()

# Plot heatmap
sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.8}
)

plt.title("Correlation Heatmap", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig("plots/correlation_heatmap.png")
plt.show()
