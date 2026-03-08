import shap
import joblib
import matplotlib.pyplot as plt

def explain_prediction(model_path, patient_data):
    """
    Generates a SHAP explanation for an individual patient's diagnostic score.
    """
    model = joblib.load(model_path)
    
    # Initialize KernelExplainer (works for any model type: XGBoost, SVM, NN)
    explainer = shap.Explainer(model)
    shap_values = explainer(patient_data)
    
    # Global Summary Plot
    plt.figure()
    shap.summary_plot(shap_values, patient_data, show=False)
    plt.title("Global Feature Importance (ArbudaMukt Diagnostic)")
    plt.savefig('../web_app/assets/shap_summary.png')
    
    # Local Waterfall Plot (for the specific patient)
    plt.figure()
    shap.plots.waterfall(shap_values[0], show=False)
    plt.title("Individual Risk Attribution")
    plt.savefig('../web_app/assets/patient_explanation.png')
    
    return shap_values

print(" Statistical XAI Agent (Arbuda-SHAP) initialized.")
