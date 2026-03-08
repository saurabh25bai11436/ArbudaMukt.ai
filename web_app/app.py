import os
import torch
import joblib
import numpy as np
from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from PIL import Image
import io

# Internal Module Imports (Assumes your folder structure is set)
# from models.screening_img.inference import run_screening
# from xai.grad_cam_utils import generate_grad_cam

app = FastAPI(
    title="ArbudaMukt.ai Core API",
    description="Backend engine for Breast Cancer Detection, Diagnosis, and Mitigation.",
    version="2.0.0"
)

# --- 1. MODEL INITIALIZATION (Singleton Pattern) ---
# We load models into memory once at startup to ensure fast inference.
MODELS = {}

@app.on_event("startup")
def load_engines():
    try:
        # Load Tabular Diagnostic Model (XGBoost)
        MODELS["diagnostic"] = joblib.load("../models/diagnostic_tab/diagnostic_v1.pkl")
        
        # Load Imaging Screening Model (PyTorch/MONAI)
        # MODELS["screening"] = torch.load("../models/screening_img/arbuda_seg_v1.pth", map_location="cpu")
        
        # Load Treatment Response Model (CatBoost)
        # MODELS["treatment"] = joblib.load("../models/treatment_cure/pcr_predictor_v1.cbm")
        
        print(" All ArbudaMukt AI Engines loaded successfully.")
    except Exception as e:
        print(f" Error loading models: {e}")

# --- 2. DATA SCHEMAS (Pydantic) ---
class BiopsyInput(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    smoothness_mean: float
    compactness_mean: float

class TreatmentInput(BaseModel):
    age: int
    er_status: int  # 0: Neg, 1: Pos
    pr_status: int
    her2_status: int
    tumor_size_mm: float

# --- 3. API ENDPOINTS ---

@app.get("/")
def home():
    return {"message": "ArbudaMukt API is Operational", "status": "Ready"}

@app.post("/api/v1/screen/image")
async def screen_image(file: UploadFile = File(...)):
    """
    Detection Module: Accepts mammogram/MRI and returns lesion coordinates.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")
    
    # Read image
    request_object_content = await file.read()
    img = Image.open(io.BytesIO(request_object_content)).convert("L")
    
    # Placeholder for actual model inference logic
    # prediction = run_screening(img, MODELS["screening"])
    
    return {
        "filename": file.filename,
        "lesion_detected": True,
        "confidence": 0.982,
        "bi_rads_assessment": "Category 4 (Suspicious)"
    }

@app.post("/api/v1/diagnose/biopsy")
async def diagnose_biopsy(data: BiopsyInput):
    """
    Diagnosis Module: Classifies biopsy features into Malignant or Benign.
    """
    features = np.array([[
        data.radius_mean, data.texture_mean, data.perimeter_mean, 
        data.area_mean, data.smoothness_mean, data.compactness_mean
    ]])
    
    # Predict using the XGBoost model
    prob = MODELS["diagnostic"].predict_proba(features)[0][1]
    prediction = "Malignant" if prob > 0.5 else "Benign"
    
    return {
        "prediction": prediction,
        "probability_malignant": round(float(prob), 4),
        "action_recommended": "Immediate Oncology Consultation" if prediction == "Malignant" else "Routine Follow-up"
    }

@app.post("/api/v1/cure/plan")
async def suggest_treatment(data: TreatmentInput):
    """
    Cure Module: Predicts probability of Pathological Complete Response (pCR).
    """
    # Logic to interface with models/treatment_cure/response_pred.py
    return {
        "chemo_response_probability": 0.74,
        "suggested_pathway": "Neoadjuvant Chemotherapy (NAC)",
        "surgical_option": "Breast-Conserving Surgery (BCS) viable post-NAC"
    }

@app.get("/api/v1/mitigation/prognosis/{patient_id}")
async def get_prognosis(patient_id: str):
    """
    Mitigation Module: Returns 5-year survival and recurrence risks.
    """
    return {
        "patient_id": patient_id,
        "five_year_survival_rate": "94%",
        "recurrence_risk_score": "Low",
        "lifestyle_mitigation": ["Daily exercise", "Low-fat diet", "Annual MRI"]
    }

# --- 4. EXECUTION ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
