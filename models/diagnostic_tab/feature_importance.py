import matplotlib.pyplot as plt
import xgboost as xgb
import joblib

def plot_arbuda_features(model_path='diagnostic_v1.pkl'):
    """
    Visualizes which biopsy features most impact the model's decision.
    """
    model = joblib.load(model_path)
    
    # Get feature importance based on 'weight' (frequency of use)
    importance = model.get_booster().get_score(importance_type='weight')
    
    # Sort and plot top 15 features
    sorted_importance = dict(sorted(importance.items(), key=lambda item: item[1], reverse=True)[:15])
    
    plt.figure(figsize=(10, 6))
    plt.barh(list(sorted_importance.keys()), list(sorted_importance.values()), color='skyblue')
    plt.xlabel('Importance Score (Frequency of Splits)')
    plt.title('ArbudaMukt Diagnostic: Top 15 Clinical Indicators')
    plt.gca().invert_yaxis()
    plt.show()

if __name__ == "__main__":
    plot_arbuda_features()
