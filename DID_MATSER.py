import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('DiD_master_data.csv')
print("--- Step 1: Master data file loaded successfully. ---")
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y', errors='coerce')#date time format
df['export_value'] = pd.to_numeric(df['export_value'], errors='coerce')#convert to num
df.dropna(subset=['date', 'export_value'], inplace=True)#drop na
print("Data types converted successfully.")


policy_date = pd.to_datetime('2025-04-05')#The date the policy was applied

df['time'] = (df['date'] >= policy_date).astype(int)# Create the time Dummy Variable
print(f"'time' variable created based on policy date {policy_date.date()} ---")
print(f"Data spans from {df['date'].min().date()} to {df['date'].max().date()}.")

try:
    
    #Parallel Plot
    # Using the pivot_table method
    df_pivot = df.pivot_table(index='date', columns='treat', values='export_value', aggfunc='mean')
    df_plot = df_pivot.reset_index().melt(id_vars='date', var_name='treat', value_name='export_value')
    #labels
    df_plot['Group'] = df_plot['treat'].apply(
        lambda x: 'Treatment (Iron & Steel)' if x == 1 else 'Control (Semiconductors)')

    plt.figure(figsize=(12, 8))
    sns.lineplot(data=df_plot, x='date', y='export_value', hue='Group', marker='o')
    plt.axvline(x=policy_date, color='red', linestyle='--', label=f'Policy Implemented ({policy_date.date()})')
    plt.title('Parallel Trends Check: Average Monthly Exports', fontsize=16)
    plt.ylabel('Average Export Value', fontsize=12)
    plt.xlabel('Date', fontsize=12)
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.show()
    plt.savefig('parallel_trends_plot_2024_2025.png')
    print("--- Plot generated and saved as 'parallel_trends_plot_2024_2025.png' ---")

except Exception as e:
    print(f"\nPlotting failed with error: {e}")


    print("\nERROR: No data left to analyze.")
else:
    model_formula = 'export_value ~ treat + time + treat:time'
    did_model = smf.ols(model_formula, data=df).fit()

    print(" Step 4: DiD Regression Results")
    print(did_model.summary())

