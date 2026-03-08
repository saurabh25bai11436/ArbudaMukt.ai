import requests
import os                                                                                                

def download_tcia_collection(collection_name="CBIS-DDSM"):
    # Note: Requires 'tcia-utils' or direct REST API access
    api_url = f"https://services.cancerimagingarchive.net/nbia-api/services/v1/getSeries?Collection={collection_name}"
    
    print(f" Querying {collection_name} from TCIA...")
    response = requests.get(api_url)
    
    if response.status_code == 200:
        # In a real scenario, you'd iterate through series UIDs and download DICOMs
        # For the repo, we provide a placeholder to the NBIA Data Retriever link
        print(" TCIA Collections require the NBIA Data Retriever.")
        print(" Download the manifest here: https://www.cancerimagingarchive.net/collection/cbis-ddsm/")
    else:
        print(" Error connecting to TCIA API.")

if __name__ == "__main__":
    download_tcia_collection()
