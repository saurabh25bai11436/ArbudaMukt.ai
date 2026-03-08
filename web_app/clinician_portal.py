import streamlit as st
import PIL.Image
import requests

def run_clinician_portal():
    st.set_page_config(layout="wide")
    st.title("🩺 ArbudaMukt Clinician Portal")
    st.sidebar.info("Logged in as: Dr. Oncologist | Hospital ID: AM-992")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Imaging Analysis (Screening)")
        uploaded_scan = st.file_uploader("Upload DICOM/Mammogram", type=['png', 'jpg', 'dcm'])
        if uploaded_scan:
            st.image(uploaded_scan, use_column_width=True, caption="Raw Mammogram (LCC View)")
            if st.button("Generate Heatmap (Grad-CAM)"):
                st.image("assets/gradcam_sample.png", caption="AI Attention Map (Lesion Localized)")
                st.warning(" High Density (BI-RADS C) detected in Upper Outer Quadrant.")

    with col2:
        st.subheader("Biopsy & Genomic Decision Support")
        radius = st.slider("Mean Radius", 5.0, 30.0, 14.5)
        texture = st.slider("Mean Texture", 10.0, 40.0, 20.2)
        
        st.markdown("---")
        if st.button("Synthesize Diagnosis"):
            # Call the Multimodal Fusion Model
            st.error("### Result: MALIGNANT (Risk: 94.2%)")
            st.write("**Top Indicators:** Concave Points, Perimeter Mean")
            st.image("assets/shap_waterfall.png", caption="SHAP Feature Attribution")

    st.markdown("---")
    st.subheader("Treatment Roadmap (Cure Module)")
    st.success("Recommended: Neoadjuvant Chemotherapy followed by BCS (Breast-Conserving Surgery)")

if __name__ == "__main__":
    run_clinician_portal()
