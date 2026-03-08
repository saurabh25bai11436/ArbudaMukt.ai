#  Ethical AI Framework

## 1. Bias Mitigation
We acknowledge that breast cancer presentation varies across ethnicities (e.g., higher prevalence of Triple-Negative Breast Cancer in Black women). 
* **Action:** Our dataset is audited for representation across BI-RADS density scores and demographic backgrounds.

## 2. Human-in-the-Loop (HITL)
ArbudaMukt is a **Decision Support System**, not a diagnostic replacement.
* **Protocol:** All AI predictions must be signed off by a licensed radiologist or oncologist.
* **Fallback:** If confidence scores are below 75%, the system automatically triggers a "Manual Review Required" flag.

## 3. Transparency
We use SHAP and Grad-CAM to ensure that the AI's "logic" is visible to the clinician, preventing "Black Box" errors.
