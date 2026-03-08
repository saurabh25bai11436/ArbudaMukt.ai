import cv2
import numpy as np
import os

def normalize_and_resize(image_path, target_size=(224, 224)):
    """
    Standardizes medical images for Deep Learning models.
    """
    # Load image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None

    # 1. Intensity Normalization (Min-Max Scaling to [0, 1])
    img_normalized = img.astype(np.float32) / 255.0

    # 2. Resize using Bilinear Interpolation
    img_resized = cv2.resize(img_normalized, target_size, interpolation=cv2.INTER_LINEAR)

    # 3. CLAHE (Contrast Limited Adaptive Histogram Equalization)
    # Improves visibility of microcalcifications
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img_uint8 = (img_resized * 255).astype(np.uint8)
    img_enhanced = clahe.apply(img_uint8)

    return img_enhanced / 255.0

print(" Image standardization module ready.")
