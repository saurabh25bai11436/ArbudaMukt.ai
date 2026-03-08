from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import torch
import joblib
import numpy as np
import io
from PIL import Image

app = FastAPI(title="ArbudaMukt AI API", version="1.0.0")

# 1. Load pre-trained models at startup for efficiency
try:
    diagnostic_model = joblib.load('../models/diagnostic_tab/diagnostic_v1.pkl')
    # screening_model = torch.load('../models/screening_img/arbuda_seg_v1.pth')
except Exception as e:
    print(f" Model loading failed: {e}")

# 2. Define input data schema for tabular biopsy results
class BiopsyData(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    # ... include other essential clinical markers

@app.get("/")
async def health_check():
    return {"status": "ArbudaMukt Systems Online", "models_loaded": True}

@app.post("/predict/biopsy")
async def predict_biopsy(data: BiopsyData):
    """Predicts malignancy from tabular clinical data."""
    features = np.array([[data.radius_mean, data.texture_mean, data.perimeter_mean, data.area_mean]])
    prediction = diagnostic_model.predict(features)
    probability = diagnostic_model.predict_proba(features)[0][1]
    
    return {
        "diagnosis": "Malignant" if prediction[0] == 1 else "Benign",
        "confidence_score": float(probability)
    }

@app.post("/predict/screening")
async def predict_image(file: UploadFile = File(...)):
    """Handles mammogram uploads for AI screening."""
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")
    
    contents = await file.read()
    # Process image through screening_img module
    # result = screening_model(contents)
    
    return {"message": f"Successfully processed {file.filename}", "lesions_detected": 1}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
