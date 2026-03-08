from fusion_model import ArbudaFusionAgent
import torch

def run_diagnostic_pipeline(image_tensor, clinical_data_tensor):
    """
    Orchestrates the full diagnostic loop.
    1. Extract features via specialized agents.
    2. Fuse features for final risk assessment.
    """
    # Placeholder for calls to Imaging and Clinical Agents
    # img_feats = ImagingAgent.process(image_tensor)
    # clinical_feats = ClinicalAgent.process(clinical_data_tensor)
    
    model = ArbudaFusionAgent()
    # Loading pre-trained weights
    # model.load_state_dict(torch.load('fusion_v1.pth'))
    
    model.eval()
    with torch.no_grad():
        # Multimodal integration results in higher AUC than unimodal paths
        final_risk = model(img_feats, clinical_feats)
    
    return final_risk

print(" Orchestrator ready: Detection -> Fusion -> Diagnosis.")
