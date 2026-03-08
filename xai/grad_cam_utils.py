import torch
import torch.nn.functional as F
import cv2
import numpy as np

def generate_grad_cam(model, input_image, target_layer):
    """
    Produces a Grad-CAM heatmap to visualize 'attention' on a mammogram.
    """
    model.eval()
    
    # 1. Capture gradients during forward/backward pass
    gradients = []
    activations = []

    def save_gradient(grad):
        gradients.append(grad)

    def forward_hook(module, input, output):
        activations.append(output)
        output.register_hook(save_gradient)

    handle = target_layer.register_forward_hook(forward_hook)

    # 2. Forward pass
    output = model(input_image)
    category_index = torch.argmax(output)

    # 3. Backward pass
    model.zero_grad()
    output[0, category_index].backward()

    # 4. Generate Heatmap
    pooled_gradients = torch.mean(gradients[0], dim=[0, 2, 3])
    for i in range(activations[0].shape[1]):
        activations[0][:, i, :, :] *= pooled_gradients[i]
    
    heatmap = torch.mean(activations[0], dim=1).squeeze().detach().numpy()
    heatmap = np.maximum(heatmap, 0) # ReLU on heatmap
    heatmap /= np.max(heatmap)
    
    handle.remove()
    return heatmap

def overlay_heatmap(original_img, heatmap):
    """Applies the heatmap onto the grayscale mammogram."""
    heatmap = cv2.resize(heatmap, (original_img.shape[1], original_img.shape[0]))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    
    # Superimpose the heatmap with 40% opacity
    superimposed_img = heatmap * 0.4 + original_img
    return superimposed_img

print("📸 Visual XAI Agent (Arbuda-GradCAM) initialized.")
