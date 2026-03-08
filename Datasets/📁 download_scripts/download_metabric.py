import os
import requests

def download_metabric():
    # METABRIC Study ID on cBioPortal
    study_id = "brca_metabric"
    url = f"https://www.cbioportal.org/api/studies/{study_id}/clinical-data?retrievalMode=ALL&sampleService-filter=%7B%7D"
    
    print("🧬 Fetching METABRIC Treatment & Survival Data...")
    response = requests.get(url)
    
    if response.status_code == 200:
        os.makedirs("../raw", exist_ok=True)
        with open("../raw/metabric_clinical.json", "w") as f:
            f.write(response.text)
        print(" Success! METABRIC clinical data saved.")
    else:
        print(f" Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    download_metabric()
