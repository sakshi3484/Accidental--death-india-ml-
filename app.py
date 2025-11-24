import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Indian Accident Risk Predictor", page_icon="🚦", layout="centered")

# ----------------------------
# Sidebar: Project Links & About
# ----------------------------
st.sidebar.title("Project Links")

# Colab notebook link
st.sidebar.markdown(
    "[📄 View Full Notebook on Google Colab](https://colab.research.google.com/drive/1G-zgDZCNR_gz3PYv_ipddt-aqPleGq-B)"
)




st.sidebar.markdown("---")
st.sidebar.title("About this App")
st.sidebar.write(
    "This tool predicts the risk level of traffic accident deaths for a region in India "
    "based on historical accident statistics from ADSI reports."
)

st.sidebar.markdown(
    "**Risk Levels:**\n"
    "- Low: fewer fatalities predicted\n"
    "- Medium: moderate fatality risk\n"
    "- High: severe fatality risk\n\n"
    "**Data Source:** ADSI (Accidental Deaths & Suicides in India), Govt. of India."
)

# ----------------------------
# Main Input Form
# ----------------------------
st.title("Deaths in India")
st.write("Enter accident statistics to estimate traffic accident deaths and get a risk rating for your region.")

road_cases = st.number_input("🚗 Road Accidents - Cases", min_value=0)
road_injured = st.number_input("🚗 Road Accidents - Injured", min_value=0)
road_died = st.number_input("🚗 Road Accidents - Died", min_value=0)

rail_cases = st.number_input("🚆 Railway Accidents - Cases", min_value=0)
rail_injured = st.number_input("🚆 Railway Accidents - Injured", min_value=0)
rail_died = st.number_input("🚆 Railway Accidents - Died", min_value=0)

cross_cases = st.number_input("⚠️ Railway Crossing Accidents - Cases", min_value=0)
cross_injured = st.number_input("⚠️ Railway Crossing Accidents - Injured", min_value=0)
cross_died = st.number_input("⚠️ Railway Crossing Accidents - Died", min_value=0)

total_cases = st.number_input("📊 Total Traffic Accidents - Cases", min_value=0)
total_injured = st.number_input("📊 Total Traffic Accidents - Injured", min_value=0)

if st.button("Predict"):
    # Example prediction (replace with your ML model later)
    predicted_deaths = road_died + rail_died + cross_died
    st.success(f"**Predicted Deaths:** {predicted_deaths}")

    if predicted_deaths < 50:
        st.markdown("✅ **Low Risk**", unsafe_allow_html=True)
    elif predicted_deaths < 200:
        st.markdown("🟡 **Medium Risk**", unsafe_allow_html=True)
    else:
        st.markdown("🔴 **High Risk**", unsafe_allow_html=True)
