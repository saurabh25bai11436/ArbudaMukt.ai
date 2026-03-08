#  Real-World Clinician Feedback & Correction Log

## 1. Purpose
This log captures instances where a human expert (Radiologist/Oncologist) overruled the AI prediction. These "Hard Samples" are prioritized for model re-training to reduce False Positives/Negatives.

## 2. Correction Registry

| Entry ID | Date | Module | AI Prediction | Human Correction | Reason for Error |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FB-001 | 2026-03-01 | Detection | Malignant | **Benign** | AI flagged post-surgical scarring as a new lesion. |
| FB-002 | 2026-03-04 | Diagnosis | Benign | **Malignant** | Micropapillary features missed; subtle genomic markers over-weighted by AI. |
| FB-003 | 2026-03-08 | Cure | High pCR | **Low pCR** | Patient's comorbid cardiac condition limits aggressive chemo dosage. |

## 3. Active Learning Pipeline Status
* **Pending Samples:** 12 cases flagged for review.
* **Retraining Trigger:** Scheduled for 50 verified corrections.
* **Current Model Version:** v2.0.4 (Includes fixes for vascular calcification misidentification).

## 4. Instructions for Clinicians
To log a correction, use the **"Flag Result"** button in the `web_app/clinician_portal.py`. Please include:
1. The unique Patient Hash.
2. Description of the artifact or clinical nuance the AI missed.
3. Relevant pathology report scan.
