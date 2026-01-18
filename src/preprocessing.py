import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    X = df.drop("MEDV", axis=1)
    y = df["MEDV"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)

    return X_scaled_df, y, scaler
