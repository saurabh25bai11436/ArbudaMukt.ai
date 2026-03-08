import pydicom
import numpy as np

def process_dicom(dicom_path):
    """
    Extracts pixel data and removes PHI metadata.
    """
    ds = pydicom.dcmread(dicom_path)
    
    # Extract Pixel Array
    pixel_data = ds.pixel_array
    
    # Handle Photometric Interpretation (Invert if MONOCHROME1)
    if ds.PhotometricInterpretation == "MONOCHROME1":
        pixel_data = np.amax(pixel_data) - pixel_data
        
    # Standardize to 8-bit for preview
    pixel_data = ((pixel_data - np.min(pixel_data)) / (np.max(pixel_data) - np.min(pixel_data)) * 255).astype(np.uint8)
    
    return pixel_data

print(" DICOM processing module ready.")
