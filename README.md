# Analysis of Usage-Based Insurance (UBI) Adoption Behavior

## 📌 Project Overview
This repository contains the computational framework and statistical models developed for my Master's thesis in Transportation Engineering. The study investigates the behavioral factors influencing the adoption of **Usage-Based Insurance (UBI)** schemes among heavy vehicle drivers in Iran.

The research utilizes a **mixed-method econometric approach**, leveraging the specific strengths of different statistical tools to analyze distinct aspects of driver behavior:
1.  **Panel Data Analysis:** To account for unobserved heterogeneity in repeated choice scenarios.
2.  **Survival Analysis:** To model the "time-to-acceptance" and decision-making speed.

---

## 📂 Repository Structure

The project is organized into two main modeling modules:

| Module | Tool | Methodology | Key Objectives |
| :--- | :--- | :--- | :--- |
| **1. Econometric Modeling** | **Stata 17** | Random Effects Logit | Analyzing choice heterogeneity & willingness-to-accept (WTA). |
| **2. Survival Analysis** | **Python** | Cox Proportional Hazards | Investigating the impact of covariates on decision latency. |

---

## 📊 Module 1: Random Effects Logistic Regression (Stata)
**Location:** `/1_Stata_Code`

This module addresses the panel nature of the Stated Preference (SP) data, where each respondent faced multiple choice scenarios. Standard logit models often fail to capture the correlation of error terms for the same individual. Therefore, a **Random Effects (RE)** framework was implemented.

### Files Description:
* `model_app_re.do`:
    * **Scenario:** Adoption of a UBI smartphone application.
    * **Logic:** Estimates the probability of app acceptance based on monetary incentives (payment per km) and driver characteristics.
    * **Output:** Marginal effects of payment levels on adoption probability.

* `model_supervisor_re.do`:
    * **Scenario:** Adoption of a hardware-based monitoring system (Driver-Facing Camera).
    * **Logic:** Analyzes the trade-off between privacy concerns (surveillance) and financial benefits (insurance discounts).
    * **Output:** Quantifies the "disutility" of being monitored.

---

## 🐍 Module 2: Hazard & Survival Modeling (Python)
**Location:** `/2_Python_Code` (or root directory)

While Stata was used for choice probability, Python was employed to analyze the **temporal dimension** of the decision. Using the `lifelines` library, I modeled the "Time-to-Event" (time until a driver accepts a UBI offer).

### Files Description:
* `app_acceptance_model.ipynb` (Jupyter Notebook):
    * **Method:** Cox Proportional Hazards Model.
    * **Key Features:**
        * Implementation of semi-parametric survival analysis.
        * Calculation of **Hazard Ratios (HR)** to interpret covariate impacts.
        * Visualization of percentage changes in hazard rates using `Matplotlib` and `Seaborn`.
    * **Insight:** Identifies which demographic factors (e.g., age, cargo type) accelerate or decelerate the adoption decision.

---

## ⚠️ Data Privacy & Reproducibility Note
To protect the privacy of the survey participants (truck drivers) and comply with ethical research guidelines, the **original dataset is not included** in this repository.

* **Sample Data:** The scripts formated to run on `sample_data.csv` (provided in the repo). This file contains synthetic/dummy data with the same structure (columns and data types) as the original dataset.
* **Reproducibility:** Researchers can verify the model logic, code structure, and visualization outputs using this sample data.

---

## 📧 Contact
**Mohammadreza Khodaverdi**
* Research Interests: Choice Modeling, Road Safety, UBI, ITS.
* Email: khodaverdi.mohammadreza11@gmail.com
* LinkedIn: linkedin.com/in/mohammadreza-khodaverdi
