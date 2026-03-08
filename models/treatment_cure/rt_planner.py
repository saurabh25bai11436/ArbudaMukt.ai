import torch
import torch.nn as nn

class DosePredictionNet(nn.Module):
    """
    U-Net based architecture for predicting 3D radiation dose distributions.
    Aims to optimize 'healthy tissue sparing' (Lungs/Heart).
    """
    def __init__(self):
        super(DosePredictionNet, self).__init__()
        # Simplified U-Net for dose mapping from CT anatomy to Dose Grid
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(64, 1, kernel_size=2, stride=2),
            nn.Sigmoid() # Normalize dose 0 to 1
        )

    def forward(self, x):
        x = self.encoder(x)
        return self.decoder(x)

def predict_cardiac_risk(mean_heart_dose):
    """Flags cases requiring Deep Inspiration Breath-Hold (DIBH) techniques."""
    threshold = 1.0 # Gy (Threshold for high cardiac risk)
    return "HIGH RISK: Recommend DIBH" if mean_heart_dose > threshold else "STANDARD PROTOCOL"

print(" Radiotherapy planning module (Arbuda-RT) initialized.")
