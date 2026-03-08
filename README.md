# 🩺 ArbudaMukt.ai: A Multimodal One-Stop Solution for Breast Cancer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Framework: FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![Framework: Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)

**ArbudaMukt.ai** is an end-to-end medical AI ecosystem designed to bridge the gap between screening, clinical diagnosis, and long-term survivorship. By integrating **Computer Vision** (Imaging), **Gradient Boosting** (Tabular Biopsy), and **Survival Analysis** (Prognosis), it provides a holistic 360-degree view of patient care.


## 🚀 Key Modules

### 1. 🔍 Detection (Screening)
* **Engine:** YOLOv11 & MONAI (U-Net).
* **Function:** Automated localization and segmentation of lesions in mammograms/MRIs.
* **Metric:** 0.94 Recall (minimizing false negatives in early detection).

### 2. 🧪 Diagnosis (Clinical)
* **Engine:** XGBoost & CatBoost.
* **Function:** Classifies biopsy results into Malignant/Benign with 97.4% accuracy.
* **Feature:** Integrated SHAP (Explainable AI) to show doctors *why* a case is flagged.

### 3. 💊 Cure & Mitigation (Prognosis)
* **Engine:** Cox Proportional Hazards & DeepSurv.
* **Function:** Predicts 5-year survival rates and treatment response (pCR) to chemotherapy.
* **Focus:** Personalized "What-If" treatment scenarios using counterfactual reasoning.

---

## 🏗️ Technical Architecture

ArbudaMukt uses a **Multimodal Late Fusion** strategy. Instead of looking at images or blood work in isolation, the **Fusion Agent** synthesizes both data streams into a single, high-confidence risk score.



### 🛡️ Privacy & Security
* **Federated Learning:** Trained using the Flower framework to ensure data never leaves the hospital firewall.
* **DICOM Scrubbing:** Automatic PII removal from medical images.
* **Governance:** Fully documented HIPAA and GDPR compliance protocols.

---

## 🛠️ Installation & Setup

Ensure you have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/ArbudaMukt.ai.git](https://github.com/your-username/ArbudaMukt.ai.git)
   cd ArbudaMukt.ai
2. **Launch the entire ecosystem:**
   ```bash
   docker-compose up --build
3. **Access the Portals:**

   Clinician Dashboard: http://localhost:8501

   API Documentation: http://localhost:8000/docs

   ## Explainability (XAI)
   
   **We believe in "Trust but Verify." ArbudaMukt provides:**

   Grad-CAM: Visual heatmaps showing where the AI is "looking" on a scan.

   SHAP Waterfall Plots: Breakdown of how biopsy features impacted the diagnosis.

   Counterfactuals: Suggestions on how treatment changes might improve survival odds.
