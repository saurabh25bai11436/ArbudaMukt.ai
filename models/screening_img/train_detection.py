from ultralytics import YOLO
import os

def train_lesion_detector():
    """
    Trains a YOLOv8/v11 model to detect and bound breast lesions.
    """
    # 1. Initialize Model (using pre-trained weights for transfer learning)
    model = YOLO('yolov8n.pt') 

    # 2. Define Dataset Configuration (Standard YAML format)
    # Ensure datasets/preprocessing/convert_to_yolo.py has been run first
    data_config = "../../datasets/config/breast_lesions.yaml"

    print("Starting Arbuda-Det-v1 Training...")
    results = model.train(
        data=data_config,
        epochs=100,
        imgsz=640,
        batch=16,
        name='Arbuda_Lesion_Detection',
        patience=20, # Early stopping to prevent overfitting
        project='ArbudaMukt_Screening'
    )
    
    # 3. Save the best weights for deployment
    model.export(format='onnx') # Optimized for FastAPI/Production
    print("Detection model trained and exported to ONNX.")

if __name__ == "__main__":
    train_lesion_detector()
