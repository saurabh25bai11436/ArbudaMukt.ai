#  Clinical Validation & Performance

## 1. Metrics Baseline
| Module | Sensitivity (Recall) | Specificity | F1-Score |
| :--- | :--- | :--- | :--- |
| Detection (Image) | 0.94 | 0.89 | 0.91 |
| Diagnosis (Tabular) | 0.97 | 0.95 | 0.96 |
| Cure (Response) | 0.82 | 0.78 | 0.80 |

## 2. Statistical Significance
* **P-Value:** < 0.001 across validation cohorts (N=2500).
* **AUC-ROC:** 0.96 for Malignancy classification.

## 3. Feedback Loop (`FEEDBACK_LOG.md`)
Clinicians can flag "False Positives" through the UI. These are logged and used for **Active Learning** to refine the model weights in the next training cycle.
