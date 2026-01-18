import joblib
import pandas as pd

# Load saved model & scaler
model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")

# Example: NEW house data (client input)
new_house = {
    "CRIM": 0.2,
    "ZN": 18.0,
    "INDUS": 2.3,
    "CHAS": 0,
    "NX": 0.5,
    "RM": 6.5,
    "AGE": 65.0,
    "DIS": 4.2,
    "RAD": 4,
    "TAX": 300,
    "PTRATIO": 15,
    "B": 390,
    "LSTAT": 10.5
}

df_new = pd.DataFrame([new_house])

# Scale using OLD scaler
df_scaled = scaler.transform(df_new)

# Predict
prediction = model.predict(df_scaled)

print(f"Predicted house price: ${prediction[0]*1000:.2f}")
