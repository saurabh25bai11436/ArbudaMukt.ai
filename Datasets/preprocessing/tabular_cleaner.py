import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.preprocessing import StandardScaler

def clean_clinical_data(df):
    """
    Handles missing values and scales features for XGBoost/SVM.
    """
    # 1. Identify numerical columns
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns

    # 2. Advanced Imputation (MICE)
    # Predicted missing values based on other patient features
    imputer = IterativeImputer(max_iter=10, random_state=42)
    df[num_cols] = imputer.fit_transform(df[num_cols])

    # 3. Standardization (Mean=0, Std=1)
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])

    return df

print(" Clinical data cleaning module ready.")
