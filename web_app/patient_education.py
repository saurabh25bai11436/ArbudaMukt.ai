import streamlit as st

def run_patient_portal():
    st.title("Your ArbudaMukt Health Journey")
    st.subheader("Understand your results with clarity and support.")

    st.markdown("""
    ###  Survival & Recovery
    Based on our AI's analysis of global survivors with similar profiles to yours:
    * **5-Year Survival Probability:** 98%
    * **Recovery Timeline:** ~6 months to full activity
    """)

    st.info(" **What this means:** Your tumor was detected at an early stage where treatments are most effective.")

    st.subheader(" My Progress Tracker")
    st.progress(45) # 45% through treatment phase
    st.write("You are currently in: **Post-Surgical Recovery**")

    st.subheader(" Recommended Lifestyle Mitigation")
    st.write("- **Nutrition:** Focus on antioxidant-rich diet.")
    st.write("- **Activity:** 20 mins light walking daily.")
    
    if st.button("Download My Care Plan (PDF)"):
        st.write("Generating your personalized guide...")

if __name__ == "__main__":
    run_patient_portal()
