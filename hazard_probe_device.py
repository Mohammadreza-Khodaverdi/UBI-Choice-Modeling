import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from lifelines import CoxPHFitter

# --- Configuration ---
DATA_PATH = 'sample_data.csv'  # Relative path for GitHub compatibility

def load_and_prep_data(filepath):
    """
    Loads data and prepares covariates for the Cox Proportional Hazards model.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Dataset loaded successfully. Shape: {df.shape}")
        
        # 1. Feature Engineering: Convert categorical scenarios to numeric
        # Assuming 'scenario' exists. If not, ensure your dummy data has this column.
        if 'scenario' in df.columns:
            df['scenario_numeric'] = df['scenario'].apply(lambda x: 1 if x == 'probe_camera' else 0)
        
        # 2. Define Covariates (ensure these match your dummy data headers)
        covariates = [
            'scenario_numeric',
            'has_body_insurance',
            'drive_continue_over_10',
            'cargo_perishable',
            'cruise_regular'
        ]
        
        # Filter for existing columns only
        available_covariates = [col for col in covariates if col in df.columns]
        
        # Check required columns for Survival Analysis
        if 'time_to_event' not in df.columns or 'event_status' not in df.columns:
            raise ValueError("Data must contain 'time_to_event' and 'event_status' columns.")
            
        model_df = df[['time_to_event', 'event_status'] + available_covariates].dropna()
        return model_df, available_covariates

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Please upload 'sample_data.csv'.")
        return None, None

def fit_cox_model(df, covariates):
    """
    Fits the Cox Proportional Hazards model and prints the summary.
    """
    cph = CoxPHFitter()
    print("\n--- Fitting Cox Proportional Hazards Model ---")
    
    cph.fit(df, duration_col='time_to_event', event_col='event_status')
    cph.print_summary(decimals=4)
    
    return cph

def plot_hazard_ratios(cph):
    """
    Visualizes the Hazard Ratios (HR) for easy interpretation.
    """
    # Extract Hazard Ratios and Confidence Intervals
    summary_df = cph.summary.reset_index()
    summary_df['HR_Change_Pct'] = (np.exp(summary_df['coef']) - 1) * 100
    
    # Sort for better visualization
    plot_df = summary_df.sort_values('HR_Change_Pct', ascending=False)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    palette = ['green' if x > 0 else 'red' for x in plot_df['HR_Change_Pct']]
    
    ax = sns.barplot(
        x='HR_Change_Pct', 
        y='covariate', 
        data=plot_df, 
        palette=palette
    )
    
    # Aesthetics
    plt.title('Impact of Factors on Acceptance Hazard Rate (%)', fontsize=14)
    plt.xlabel('Percentage Change in Hazard Rate (%)', fontsize=12)
    plt.ylabel('Covariate', fontsize=12)
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.grid(axis='x', alpha=0.3)
    
    # Add labels
    for i, row in plot_df.iterrows():
        val = row['HR_Change_Pct']
        ax.text(
            val + (1 if val > 0 else -1), 
            i, 
            f"{val:.1f}%", 
            va='center', 
            ha='left' if val > 0 else 'right'
        )
    
    plt.tight_layout()
    plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    # 1. Load Data
    model_data, final_covariates = load_and_prep_data(DATA_PATH)
    
    if model_data is not None and not model_data.empty:
        # 2. Run Model
        cph_model = fit_cox_model(model_data, final_covariates)
        
        # 3. Check Assumptions (Optional but recommended)
        # cph_model.check_assumptions(model_data)
        
        # 4. Plot Results
        plot_hazard_ratios(cph_model)