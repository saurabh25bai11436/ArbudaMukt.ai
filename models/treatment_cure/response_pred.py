from catboost import CatBoostClassifier, Pool
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score
import pandas as pd

class ArbudaResponsePredictor:
    def __init__(self):
        # CatBoost is excellent for clinical data with categorical features (ER, PR, HER2 status)
        self.model = CatBoostClassifier(
            iterations=500,
            learning_rate=0.05,
            depth=6,
            loss_function='Logloss',
            verbose=False,
            random_seed=42
        )

    def train_pcr_model(self, data_path):
        """
        Trains model to predict if Neoadjuvant Chemotherapy (NAC) will result in pCR.
        Key features include sTILs, Ki-67, and molecular subtypes.
        """
        df = pd.read_csv(data_path)
        
        # Clinical markers prioritized by current research
        features = ['age', 'menopausal_status', 'ER_status', 'PR_status', 
                    'HER2_status', 'Ki67_expression', 'sTILs_percentage']
        X = df[features]
        y = df['pCR_outcome'] # 1 for complete response, 0 for residual disease

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

        print(" Training Neoadjuvant Response Engine...")
        self.model.fit(X_train, y_train, eval_set=(X_test, y_test))
        
        preds = self.model.predict_proba(X_test)[:, 1]
        print(f" Training Complete. Validation AUC: {roc_auc_score(y_test, preds):.4f}")

    def save(self, path='pcr_predictor_v1.cbm'):
        self.model.save_model(path)

if __name__ == "__main__":
    predictor = ArbudaResponsePredictor()
    # predictor.train_pcr_model('../../datasets/processed/treatment_data.csv')
