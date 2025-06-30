import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Ensure folders exist
os.makedirs("plots", exist_ok=True)
os.makedirs("models", exist_ok=True)

# Load cleaned data
df = pd.read_csv("cleaned_ghg_data.csv")

# Drop extra column if exists
if 'Unnamed: 7' in df.columns:
    df.drop(columns=['Unnamed: 7'], inplace=True)

# Encode Categorical Columns
df['Substance'] = df['Substance'].map({'carbon dioxide': 0, 'methane': 1, 'nitrous oxide': 2, 'other GHGs': 3})
df['Unit'] = df['Unit'].map({'kg/2018 USD, purchaser price': 0, 'kg CO2e/2018 USD, purchaser price': 1})
df['Source'] = df['Source'].map({'Commodity': 0, 'Industry': 1})

# Basic Info
print("\n Dataset Info:")
print(df.info())
print("\n Null Values:")
print(df.isnull().sum())
print("\n Summary Stats:")
print(df.describe().T)

# Target Variable Distribution
plt.figure(figsize=(6, 5))
sns.histplot(df['Supply Chain Emission Factors with Margins'], bins=50, kde=True)
plt.title('Target Variable Distribution')
plt.tight_layout()
plt.savefig("plots/target_distribution.png")
plt.show()

# Top 10 Emitting Industries
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
plt.title('Top 10 Emitting Industries')
plt.xlabel('Emission Factor (kg CO2e/unit)')
plt.ylabel('Industry')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("plots/top_10_emitting_industries.png")
plt.show()

# Drop unused columns
df.drop(columns=['Name', 'Code', 'Year'], inplace=True)

# Features and Target
X = df.drop(columns=['Supply Chain Emission Factors with Margins'])
y = df['Supply Chain Emission Factors with Margins']

# Countplots
for col in ['Substance', 'Unit', 'Source']:
    plt.figure(figsize=(6, 3))
    sns.countplot(x=X[col])
    plt.title(f"Count Plot: {col}")
    plt.tight_layout()
    plt.savefig(f"plots/{col.lower()}_countplot.png")
    plt.show()

# Correlation Heatmap
plt.figure(figsize=(12, 8))
corr_matrix = df.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True, linewidths=0.5, cbar_kws={"shrink": 0.8})
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("plots/correlation_heatmap.png")
plt.show()

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("\n Features normalized.")

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
print(" Train/Test Split Done:", X_train.shape, X_test.shape)

# Model 1: Random Forest
RF_model = RandomForestRegressor(random_state=42)
RF_model.fit(X_train, y_train)
RF_y_pred = RF_model.predict(X_test)
RF_mse = mean_squared_error(y_test, RF_y_pred)
RF_rmse = np.sqrt(RF_mse)
RF_r2 = r2_score(y_test, RF_y_pred)

# Model 2: Linear Regression
LR_model = LinearRegression()
LR_model.fit(X_train, y_train)
LR_y_pred = LR_model.predict(X_test)
LR_mse = mean_squared_error(y_test, LR_y_pred)
LR_rmse = np.sqrt(LR_mse)
LR_r2 = r2_score(y_test, LR_y_pred)

# Model Comparison
comparison_df = pd.DataFrame({
    'Model': ['Random Forest', 'Linear Regression'],
    'MSE': [RF_mse, LR_mse],
    'RMSE': [RF_rmse, LR_rmse],
    'R2': [RF_r2, LR_r2]
})
print("\n📊 Model Comparison:")
print(comparison_df)

# Save the Best Model (Linear Regression)
joblib.dump(LR_model, 'models/LR_model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
print("\n Linear Regression model & scaler saved successfully!")
