import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000/predict"

st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()

        if response.status_code == 200:
            prediction = result
            st.success(f"Predicted Insurance Premium Category: **{prediction['predicted_category']}**")
            
            # Display confidence with a progress bar
            st.write("🔍 **Model Confidence:**")
            st.progress(prediction["confidence"])
            st.write(f"{prediction['confidence']:.1%}")
            
            # Display class probabilities with progress bars
            st.write("📊 **Category Probabilities:**")
            class_probs = prediction["class_probabilities"]
            
            # Sort probabilities in descending order for better visualization
            sorted_probs = sorted(class_probs.items(), key=lambda x: x[1], reverse=True)
            
            for category, probability in sorted_probs:
                col1, col2, col3 = st.columns([2, 3, 1])
                with col1:
                    st.write(f"**{category}**")
                with col2:
                    st.progress(probability)
                with col3:
                    st.write(f"{probability:.1%}")

        else:
            st.error(f"API Error: {response.status_code}")
            st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")
