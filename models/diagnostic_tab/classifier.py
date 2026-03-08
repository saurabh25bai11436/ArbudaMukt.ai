import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
import job_lib
import os

class ArbudaDiagnosticEngine:
    def __init__(self, model_path=None):
        """
        Initializes the classifier. Loads a pre-trained model if provided.
        """
        if model_path and os.path.exists(model_path):
            self.model = joblib.load(model_path)
        else:
            # Optimized hyperparameters for breast cancer diagnostic data
            self.model = xgb.XGBClassifier(
                n_estimators=100,
                max_depth=4,
                learning_rate=0.1,
                objective='binary:logistic',
                use_label_encoder=False,
                eval_metric='logloss',
                scale_pos_weight=1.6 # Balanced weight for M vs B classes
            )
        self.scaler = StandardScaler()

    def preprocess(self, X):
        """Standardizes features (Mean=0, Std=1) to improve convergence."""
        return self.scaler.fit_transform(X)

    def train(self, data_path):
        """
        Trains the XGBoost model on the provided CSV file.
        Expects a 'diagnosis' column (M=1, B=0).
        """
        df = pd.read_csv(data_path)
        X = df.drop(columns=['id', 'diagnosis', 'Unnamed: 32'], errors='ignore')
        y = df['diagnosis'].map({'M': 1, 'B': 0}) # Encoding for binary classification

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, stratify=y, random_state=42
        )

        X_train_scaled = self.preprocess(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        print(" Training Diagnostic Engine...")
        self.model.fit(X_train_scaled, y_train)

        # Evaluation
        y_pred = self.model.predict(X_test_scaled)
        print("\n Clinical Performance Report:")
        print(classification_report(y_test, y_pred))
        print(f"ROC-AUC Score: {roc_auc_score(y_test, self.model.predict_proba(X_test_scaled)[:, 1]):.4f}")

    def save_model(self, path='diagnostic_v1.pkl'):
        joblib.dump(self.model, path)
        print(f" Model saved to {path}")

if __name__ == "__main__":
    engine = ArbudaDiagnosticEngine()
    # Assuming the data download script has run
    engine.train('../../datasets/raw/uci_wisconsin_diagnostic.csv')
    engine.save_model()
