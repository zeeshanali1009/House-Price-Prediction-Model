# House-Price-Prediction-Model
[![CI - Docker Build, Dependency & Smoke Test](https://github.com/zeeshanali1009/House-Price-Prediction-Model/actions/workflows/ci.yml/badge.svg)](https://github.com/zeeshanali1009/House-Price-Prediction-Model/actions/workflows/ci.yml)

🏠 House Price Prediction System
(End-to-End Machine Learning Project)

🔗 Live App: https://house-price-prediction-model-0565656.streamlit.app/


📌 Project Overview
The House Price Prediction System is an end-to-end machine learning solution that predicts the median value of residential properties using socio-economic, environmental, and infrastructure-related features.
This project simulates a real-world client scenario where a real-estate business requires reliable and data-driven price predictions to support:
Property valuation
Investment decision-making
Market trend analysis
The system covers the complete ML lifecycle, from data preprocessing and model training to deployment via an interactive web application.

🎯 Problem Statement
Real estate pricing depends on multiple interacting factors such as location, crime rate, pollution levels, accessibility, and housing characteristics.
Manual or intuition-based estimation is often inaccurate and inconsistent.

Objective
Build a regression-based machine learning model that can:
Learn patterns from historical housing data
Predict house prices for unseen inputs
Serve predictions through a web-based interface

📊 Dataset Description
The project uses a structured housing dataset with the following features:
Feature	Description
CRIM	Per capita crime rate
ZN	Proportion of residential land zoned for large lots
INDUS	Proportion of non-retail business acres
CHAS	Charles River dummy variable
NOX	Nitric oxide concentration
RM	Average number of rooms per dwelling
AGE	Proportion of old owner-occupied units
DIS	Distance to employment centers
RAD	Accessibility to highways
TAX	Property tax rate
PTRATIO	Pupil-teacher ratio
B	Demographic indicator
LSTAT	Lower-status population percentage
MEDV	Median house value (Target)

🧠 Methodology & Workflow
1️⃣ Data Understanding & Exploration
Analyzed feature distributions
Identified relationships between predictors and target variable
Verified data quality and consistency

2️⃣ Data Preprocessing
Feature selection
Feature scaling using StandardScaler
Ensured consistent feature alignment between training and inference

3️⃣ Model Development
Implemented a regression model using Scikit-Learn
Trained on historical housing data
Evaluated using:
Mean Squared Error (MSE)
R² Score

4️⃣ Model Persistence
Saved trained model and scaler using Joblib
Enabled inference without retraining

5️⃣ Deployment
Built an interactive Streamlit web application
Users can input property features
Model predicts house price in real time

⚙️ CI/CD & Engineering Practices
This project follows production-style ML engineering practices:
✔ Dockerized application
✔ CI pipeline using GitHub Actions
✔ Automated:
Dependency installation
Docker image build
Smoke testing

✔ Status badge for pipeline visibility

🛠️ Tech Stack
Programming Language
Python

Libraries
NumPy
Pandas
Scikit-Learn
Joblib

Visualization
Matplotlib / Seaborn (EDA)

Deployment
Streamlit Community Cloud

Dev Tools
Docker
GitHub Actions
VS Code / Jupyter Notebook

🚀 Key Features
End-to-end ML pipeline
Client-ready project structure
Reusable and scalable codebase
Web-based prediction interface
CI-tested & deployment-ready

📈 Output
Accurate house price predictions for unseen data
Interactive and user-friendly web UI
Production-ready ML artifacts (model & scaler)

💼 Real-World Applications
Real estate agencies
Property investors
Housing market analysts
Decision-support pricing systems

🌟 Why This Project Matters
This project demonstrates:
Practical regression modeling
Clean ML project organization
Deployment and CI/CD knowledge
Client-oriented problem-solving approach

Freelance-ready statement:
“I can design, train, test, and deploy machine learning solutions end-to-end.”

✅ Project Status
✔ Completed
✔ Tested
✔ CI-enabled
✔ Deployed & Live

🔗 Live Demo: https://house-price-prediction-model-0565656.streamlit.app/