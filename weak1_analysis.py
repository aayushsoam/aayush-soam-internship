# Step 1: Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load Data
excel_file = 'SupplyChainEmissionFactorsforUSIndustriesCommodities.xlsx'
years = range(2010, 2017)
all_data = []

for year in years:
    print(f" Processing year: {year}")
    try:
        df_com = pd.read_excel(excel_file, sheet_name=f'{year}_Detail_Commodity')
        df_ind = pd.read_excel(excel_file, sheet_name=f'{year}_Detail_Industry')

        df_com['Source'] = 'Commodity'
        df_ind['Source'] = 'Industry'
        df_com['Year'] = df_ind['Year'] = year

        df_com.columns = df_com.columns.str.strip()
        df_ind.columns = df_ind.columns.str.strip()

        df_com.rename(columns={'Commodity Code': 'Code', 'Commodity Name': 'Name'}, inplace=True)
        df_ind.rename(columns={'Industry Code': 'Code', 'Industry Name': 'Name'}, inplace=True)

        print(f" Commodity Shape: {df_com.shape} | Industry Shape: {df_ind.shape}")
        all_data.append(pd.concat([df_com, df_ind], ignore_index=True))

    except Exception as e:
        print(f" Error in {year}: {e}")

df = pd.concat(all_data, ignore_index=True)
print(f"\n Final dataset shape: {df.shape}")
print(df.head())
print("\n  Missing Values Summary:")
print(df.isnull().sum())

# Remove empty column if exists
if 'Unnamed: 7' in df.columns:
    df.drop(columns=['Unnamed: 7'], inplace=True)

#  Save Cleaned Data
df.to_csv("cleaned_ghg_data.csv", index=False)
print(" Cleaned data saved as 'cleaned_ghg_data.csv'")
