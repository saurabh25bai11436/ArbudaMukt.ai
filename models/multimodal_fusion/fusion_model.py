import torch
import torch.nn as nn

class ArbudaFusionAgent(nn.Module):
    """
    A Multi-Agent Fusion Controller that integrates Imaging and Clinical data.
    Uses Late Fusion to maintain modality-specific strengths.
    """
    def __init__(self, img_feature_dim=512, tab_feature_dim=16, num_classes=1):
        super(ArbudaFusionAgent, self).__init__()
        
        # 1. Image Feature Bottleneck
        self.img_bottleneck = nn.Sequential(
            nn.Linear(img_feature_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.2)
        )
        
        # 2. Tabular/Clinical Feature Bottleneck
        self.tab_bottleneck = nn.Sequential(
            nn.Linear(tab_feature_dim, 32),
            nn.ReLU()
        )
        
        # 3. Decision Fusion Layer (Concatenation)
        # Fuses radiological features with clinical metadata (age, BIRADS, etc.)
        self.classifier = nn.Sequential(
            nn.Linear(128 + 32, 64),
            nn.ReLU(),
            nn.Linear(64, num_classes),
            nn.Sigmoid() # Calibrated risk score [0, 1]
        )

    def forward(self, img_features, tab_features):
        img_x = self.img_bottleneck(img_features)
        tab_x = self.tab_bottleneck(tab_features)
        
        # Late Fusion: Join modality-specific representations
        combined = torch.cat((img_x, tab_x), dim=1)
        return self.classifier(combined)

print("🧠 Multimodal Fusion Agent (Arbuda-Fusion-v1) initialized.")
