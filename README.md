# UBI-Choice-Modeling
## 📊 Modeling Methodology
To ensure robustness and leverage specific analytical strengths, I employed a hybrid modeling approach:

### 1. Random Effects Models (Stata)
* **Objective:** To account for unobserved heterogeneity across individual drivers over repeated choice scenarios.
* **Tool:** Stata 17
* **File:** `1_Stata_RandomEffects/model_re.do`

### 2. Hazard / Survival Models (Python)
* **Objective:** To analyze the "Time-to-Event" (time until acceptance of UBI offer) and investigate the impact of covariates on the hazard rate.
* **Tool:** Python (Lifelines library)
* **File:** `2_Python_HazardModels/hazard_model.ipynb`
* **Highlights:** * Implemented Cox Proportional Hazards Model.
    * Calculated Marginal Effects and Elasticities manually.
    * Visualized Hazard Ratios using Matplotlib/Seaborn.
