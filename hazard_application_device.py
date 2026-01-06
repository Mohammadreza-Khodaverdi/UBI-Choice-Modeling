import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from lifelines import CoxPHFitter

# --- Configuration ---
# نکته مهم: در گیت‌هاب همیشه از فایل نمونه استفاده کنید
DATA_PATH = 'sample_data.csv' 

def load_and_prep_data(filepath):
    """
    Loads data and prepares covariates for the App Acceptance Hazard Model.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"✅ Dataset loaded successfully. Shape: {df.shape}")
        
        # Define expected covariates based on your study
        expected_covariates = [
            'has_body_insurance',
            'drive_continue_over_10',
            'cargo_perishable',
            'cruise_regular'
            # Add other columns present in your dummy data here
        ]
        
        # Filter for existing columns only
        available_covariates = [col for col in expected_covariates if col in df.columns]
        
        if not available_covariates:
            raise ValueError("None of the expected covariates were found in the dataset.")

        # Check required columns
        if 'time_to_event' not in df.columns or 'event_status' not in df.columns:
            raise ValueError("Data must contain 'time_to_event' and 'event_status' columns.")
            
        # Clean data
        model_df = df[['time_to_event', 'event_status'] + available_covariates].dropna()
        print(f"ℹ️ Modeling with {len(model_df)} rows (cleaned). Events observed: {model_df['event_status'].sum()}")
        
        return model_df, available_covariates

    except FileNotFoundError:
        print(f"❌ Error: The file '{filepath}' was not found. Please upload the CSV file.")
        return None, None

def fit_cox_model(df, covariates):
    """
    Fits the Cox Proportional Hazards model.
    """
    cph = CoxPHFitter()
    print("\n--- Fitting Cox Model (App Scenario) ---")
    
    # Fit the model
    cph.fit(df, duration_col='time_to_event', event_col='event_status')
    
    # Print summary
    cph.print_summary(decimals=4)
    return cph

def calculate_and_plot_results(cph):
    """
    Calculates percentage change in hazard and plots the results.
    """
    # Extract coefficients
    summary_df = cph.summary.reset_index()
    
    # Calculate percentage change: (Hazard Ratio - 1) * 100
    summary_df['HR_Change_Pct'] = (np.exp(summary_df['coef']) - 1) * 100
    
    # Sort by impact
    plot_df = summary_df.sort_values('HR_Change_Pct', ascending=False)
    
    # --- Plotting ---
    plt.figure(figsize=(12, 7))
    
    # Color logic: Green for positive impact, Red for negative
    palette = ['green' if x > 0 else 'red' for x in plot_df['HR_Change_Pct']]
    
    barplot = sns.barplot(
        x='HR_Change_Pct', 
        y='covariate', 
        data=plot_df, 
        palette=palette
    )
    
    # Labels and Titles
    plt.xlabel("Percentage Change in Hazard Rate of Acceptance (%)", fontsize=12)
    plt.ylabel("Covariate", fontsize=12)
    plt.title("Impact of Covariates on App Acceptance Hazard Rate", fontsize=14, pad=20)
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    
    # Add value labels on bars
    for i, row in plot_df.iterrows():
        val = row['HR_Change_Pct']
        # Dynamic positioning of text
        offset = 1 if val > 0 else -1
        plt.text(
            val + offset, 
            i, 
            f"{val:.1f}%", 
            va='center', 
            ha='left' if val > 0 else 'right',
            color='black',
            fontsize=10
        )

    plt.grid(axis='x', linestyle='--', alpha=0.4)
    plt.tight_layout()
    plt.show()

# --- Main Execution Block ---
if __name__ == "__main__":
    # 1. Load Data
    model_df, final_covariates = load_and_prep_data(DATA_PATH)
    
    if model_df is not None and not model_df.empty:
        # 2. Run Model
        cph_model = fit_cox_model(model_df, final_covariates)
        
        # 3. Plot Results
        calculate_and_plot_results(cph_model)