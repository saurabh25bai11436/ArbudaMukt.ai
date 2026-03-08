import pandas as pd
import os

def download_uci_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data"
    columns = [
        "id", "diagnosis", "radius_mean", "texture_mean", "perimeter_mean", "area_mean", 
        "smoothness_mean", "compactness_mean", "concavity_mean", "concave_points_mean", 
        "symmetry_mean", "fractal_dimension_mean", "radius_se", "texture_se", "perimeter_se", 
        "area_se", "smoothness_se", "compactness_se", "concavity_se", "concave_points_se", 
        "symmetry_se", "fractal_dimension_se", "radius_worst", "texture_worst", 
        "perimeter_worst", "area_worst", "smoothness_worst", "compactness_worst", 
        "concavity_worst", "concave_points_worst", "symmetry_worst", "fractal_dimension_worst"
    ]
    
    print(" Downloading UCI Wisconsin Diagnostic Dataset...")
    df = pd.read_csv(url, names=columns)
    
    os.makedirs("../raw", exist_ok=True)
    save_path = "../raw/uci_wisconsin_diagnostic.csv"
    df.to_csv(save_path, index=False)
    print(f" Success! Data saved to {save_path}")

if __name__ == "__main__":
    download_uci_data()
