import pandas as pd
from lifelines import CoxPHFitter
import matplotlib.pyplot as plt

class ArbudaSurvivalEngine:
    def __init__(self):
        self.cph = CoxPHFitter()

    def train_survival_model(self, data_path):
        """
        Trains a CoxPH model on METABRIC or clinical survival data.
        Expects columns: 'duration' (time to event) and 'event' (1=death/recurrence, 0=censored).
        """
        df = pd.read_csv(data_path)
        
        # Statistically significant covariates for breast cancer prognosis
        # Age, ER/PR status, and Tumor Stage are key indicators
        cols_to_use = ['age_at_diagnosis', 'tumor_stage', 'er_status', 
                       'pr_status', 'overall_survival_months', 'overall_survival']
        
        df_filtered = df[cols_to_use].dropna()
        
        print(" Analyzing Hazard Ratios and Survival Curves...")
        self.cph.fit(df_filtered, duration_col='overall_survival_months', event_col='overall_survival')
        self.cph.print_summary() 

    def predict_patient_curve(self, patient_data):
        """Generates an individual survival probability curve over time."""
        curve = self.cph.predict_survival_function(patient_data)
        curve.plot()
        plt.title("Individual Predicted Survival Probability")
        plt.xlabel("Months After Treatment")
        plt.ylabel("Probability of Survival")
        plt.show()

print(" Survival analysis module (Arbuda-Surv) active.")
