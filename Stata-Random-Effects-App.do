* ==============================================================================
* Project:      Usage-Based Insurance (UBI) Adoption Analysis
* Task:         Random Effects Logistic Regression (App Scenario)
* Author:       Mohammadreza Khodaverdi
* Output:       Estimates factors predicting willingness to accept UBI app
* ==============================================================================

// --- 1. Setup ---
version 17              // Ensures compatibility with Stata 17 or later
clear all               // Clear memory
set more off            // Disable pagination
macro drop _all         // Clear macros

// --- 2. Load Data ---
// Note: Ensure the dataset is in the same directory as this do-file.
// For GitHub privacy, use the provided sample dataset if real data is restricted.
import excel "app_final_dataset.xlsx", sheet("app_final_dataset") firstrow clear

// --- 3. Panel Configuration ---
// Define the panel variable (individual identifier)
xtset respondent_id

// --- 4. Model Estimation ---
// Model: Random Effects Logistic Regression
// Dependent Variable: choice (1=Accept, 0=Reject)
// Key Independent Var: level_value (Payment offered per km)
display "Running Random Effects Logistic Regression..."

xtlogit choice i.level_value ///
    ownership_full ///
    age_over_48 ///
    income_over_180m ///
    truck_type_trailer ///
    cruise_regular ///
    load_direct_owner, re

// --- 5. Marginal Effects & Visualization ---
// Calculate predicted probabilities for each payment level
margins level_value

// Plot the results
marginsplot, ///
    title("Probability of App Acceptance by Payment Level") ///
    ytitle("Predicted Probability") ///
    xtitle("Payment Level") ///
    name(graph_app, replace)

// Save the graph (Optional)
// graph export "results_app_acceptance.png", replace