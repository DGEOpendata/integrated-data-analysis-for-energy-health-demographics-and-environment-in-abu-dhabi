python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
data_energy = pd.read_csv('energy_supply_consumption_2023.csv')
data_health = pd.read_csv('covid19_case_vaccination_trends_2023.csv')
data_demographics = pd.read_csv('population_employment_demographics_2023.csv')
data_environment = pd.read_csv('air_water_quality_indices_2023.csv')
data_ghg = pd.read_csv('ghg_emissions_climate_impact_2023.csv')

# Merge datasets on location and date (assuming all datasets have these columns)
data_merged = data_energy.merge(data_health, on=['Location', 'Date'])
data_merged = data_merged.merge(data_demographics, on=['Location', 'Date'])
data_merged = data_merged.merge(data_environment, on=['Location', 'Date'])
data_merged = data_merged.merge(data_ghg, on=['Location', 'Date'])

# Example analysis: Correlation between energy consumption and GHG emissions
correlation = data_merged['Energy_Consumption'].corr(data_merged['GHG_Emissions'])
print(f'Correlation between Energy Consumption and GHG Emissions: {correlation}')

# Visualization: Trend of energy consumption vs GHG emissions over time
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Energy_Consumption', data=data_merged, label='Energy Consumption')
sns.lineplot(x='Date', y='GHG_Emissions', data=data_merged, label='GHG Emissions')
plt.title('Trend of Energy Consumption and GHG Emissions over Time')
plt.xlabel('Date')
plt.ylabel('Values')
plt.legend()
plt.show()

# Save merged dataset to a new CSV file for further analysis
data_merged.to_csv('integrated_dataset_analysis.csv', index=False)
