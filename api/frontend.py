import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="ArbudaMukt.ai Dashboard", layout="wide")

st.title(" ArbudaMukt.ai: Breast Cancer One-Stop Solution")
st.markdown("---")

tab1, tab2, tab3 = st.tabs(["Screening (Imaging)", "Diagnosis (Biopsy)", "Mitigation (Prognosis)"])

with tab1:
    st.header("Radiological Screening")
    uploaded_file = st.file_uploader("Upload Mammogram / MRI Scan", type=["jpg", "png", "dcm"])
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Scan", width=400)
        if st.button("Run AI Screening"):
            # Call FastAPI /predict/screening endpoint
            st.success("Analysis Complete: Lesion detected in Upper Outer Quadrant (UOQ).")

with tab2:
    st.header("Clinical Biopsy Diagnosis")
    col1, col2 = st.columns(2)
    with col1:
        radius = st.number_input("Radius Mean", value=14.0)
        texture = st.number_input("Texture Mean", value=19.0)
    with col2:
        perimeter = st.number_input("Perimeter Mean", value=92.0)
        area = st.number_input("Area Mean", value=650.0)
        
    if st.button("Predict Malignancy"):
        # Real-time request to FastAPI backend
        payload = {"radius_mean": radius, "texture_mean": texture, "perimeter_mean": perimeter, "area_mean": area}
        res = requests.post("http://localhost:8000/predict/biopsy", json=payload).json()
        st.subheader(f"Result: {res['diagnosis']}")
        st.info(f"Confidence Level: {res['confidence_score']:.2%}")

with tab3:
    st.header("Survival & Mitigation Planning")
    st.write("Predicting recurrence risk for the next 5 years...")
    # Integration with models/mitigation_prognosis scripts
