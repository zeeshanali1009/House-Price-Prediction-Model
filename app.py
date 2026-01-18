import streamlit as st
import pandas as pd
import joblib

# Load trained model and scaler
model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.title("House Price Prediction System")

st.write("""
### Input the house features below:
Make sure to provide values similar to the training dataset.
""")

# Create input fields for all features (match your training dataset)
CRIM = st.number_input("CRIM (per capita crime rate by town)", min_value=0.0, step=0.01)
ZN = st.number_input("ZN (proportion of residential land zoned for lots over 25,000 sq.ft.)", min_value=0.0, step=0.01)
INDUS = st.number_input("INDUS (proportion of non-retail business acres per town)", min_value=0.0, step=0.01)
CHAS = st.selectbox("CHAS (Charles River dummy variable: 1 if tract bounds river, 0 otherwise)", [0,1])
NX = st.number_input("NX (nitric oxides concentration)", min_value=0.0, step=0.001)
RM = st.number_input("RM (average number of rooms per dwelling)", min_value=0.0, step=0.01)
AGE = st.number_input("AGE (proportion of owner-occupied units built prior to 1940)", min_value=0.0, step=0.01)
DIS = st.number_input("DIS (weighted distances to five Boston employment centres)", min_value=0.0, step=0.01)
RAD = st.number_input("RAD (index of accessibility to radial highways)", min_value=0, step=1)
TAX = st.number_input("TAX (full-value property-tax rate per $10,000)", min_value=0, step=1)
PTRATIO = st.number_input("PTRATIO (pupil-teacher ratio by town)", min_value=0.0, step=0.01)
B = st.number_input("B (1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town)", min_value=0.0, step=0.01)
LSTAT = st.number_input("LSTAT (% lower status of the population)", min_value=0.0, step=0.01)

# Button for prediction
if st.button("Predict House Price"):
    # Prepare input data
    input_data = pd.DataFrame({
        'CRIM':[CRIM],
        'ZN':[ZN],
        'INDUS':[INDUS],
        'CHAS':[CHAS],
        'NX':[NX],
        'RM':[RM],
        'AGE':[AGE],
        'DIS':[DIS],
        'RAD':[RAD],
        'TAX':[TAX],
        'PTRATIO':[PTRATIO],
        'B':[B],
        'LSTAT':[LSTAT]
    })

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    st.success(f"Predicted house price: ${prediction[0]:,.2f}")
