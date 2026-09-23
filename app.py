import streamlit as st

st.title("Municipal Service Delivery Risk Predictor")

st.subheader(
    "Infrastructure Service Delivery Risk Prediction Tool"
)

st.markdown("""
This application estimates municipal service-delivery
risk based on key infrastructure indicators.
""")

water = st.number_input(
    "Water Access (%)",
    min_value=0.0,
    max_value=100.0
)

toilet = st.number_input(
    "Flush Toilet Access (%)",
    min_value=0.0,
    max_value=100.0
)

refuse = st.number_input(
    "Refuse Removal (%)",
    min_value=0.0,
    max_value=100.0
)

lighting = st.number_input(
    "Electricity Access (%)",
    min_value=0.0,
    max_value=100.0
)

if st.button("Predict Risk"):

    score = (
        water +
        toilet +
        refuse +
        lighting
    ) / 4

    if score >= 85:
        risk = "Low Risk"
        st.success(f"Predicted Risk Category: {risk}")

    elif score >= 60:
        risk = "Medium Risk"
        st.warning(f"Predicted Risk Category: {risk}")

    else:
        risk = "High Risk"
        st.error(f"Predicted Risk Category: {risk}")

    st.info(
        f"Service Score: {score:.2f}%"
    )

st.markdown("---")

st.warning(
    """
    Responsible Use Notice:

    This model is intended for educational and decision-support purposes only.

    Predictions are based on municipal service-delivery indicators and should not replace professional judgement, engineering assessments, or policy decisions.
    """
)