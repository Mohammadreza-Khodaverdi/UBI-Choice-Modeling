* ==============================================================================
* Project:      Usage-Based Insurance (UBI) Adoption Analysis
* Task:         Random Effects Logistic Regression (Supervisor/Camera Scenario)
* Author:       Mohammadreza Khodaverdi
* Output:       Estimates impact of surveillance (cameras) on UBI adoption
* ==============================================================================

// --- 1. Setup ---
version 17
clear all
set more off

// --- 2. Load Data ---
// Note: Ensure the dataset is in the same directory as this do-file.
import excel "final_supervisor_dataset.xlsx", sheet("final_supervisor_dataset") firstrow clear

// --- 3. Panel Configuration ---
xtset respondent_id

// --- 4. Model Estimation ---
// Model: Random Effects Logistic Regression
// Key Independent Var: scenario_camera (Presence of driver-facing camera)
display "Running Random Effects Logistic Regression (Surveillance Scenario)..."

xtlogit choice i.level_value ///
    scenario_camera ///
    age_over_48 ///
    income_over_180m ///
    truck_type_trailer ///
    codriver_yes, re

// --- 5. Marginal Effects & Visualization ---
// Calculate marginal effects for discount levels
margins level_value

// Plot the results to visualize the trade-off
marginsplot, ///
    title("Probability of Acceptance by Discount Level") ///
    ytitle("Predicted Probability") ///
    xtitle("Discount Level") ///
    name(graph_supervisor, replace)

// Save the graph (Optional)
// graph export "results_supervisor_acceptance.png", replace