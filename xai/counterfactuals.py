import dice_ml
from dice_ml.utils import helpers

def generate_treatment_scenarios(model, patient_df, outcome_name='recurrence_risk'):
    """
    Uses DiCE to generate 'What-If' scenarios for treatment planning.
    Example: 'If we increase chemotherapy intensity by 10%, does the risk drop?'
    """
    # 1. Create a DiCE data object
    d = dice_ml.Data(dataframe=patient_df, continuous_features=['age', 'tumor_size', 'dose'], outcome_name=outcome_name)
    
    # 2. Wrap your model
    m = dice_ml.Model(model=model, backend="sklearn")
    
    # 3. Initialize the counterfactual explainer
    exp = dice_ml.Dice(d, m, method="random")
    
    # 4. Generate 3 scenarios to show the patient
    # We fix 'age' because you can't change it, but allow 'dose' or 'surgery_type' to vary
    diverse_cf = exp.generate_counterfactuals(patient_df.iloc[0:1], total_CFs=3, desired_class="opposite",
                                              features_to_vary=["chemo_dose", "surgery_type"])
    
    return diverse_cf

print(" Counterfactual scenario generator (Arbuda-Scenario) active.")
