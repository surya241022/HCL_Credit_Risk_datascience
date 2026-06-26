

🚀 Credit Risk Scoring System

A machine learning–based Credit Risk Scoring System that predicts whether a customer is high-risk or low-risk, helping financial institutions minimize loan defaults and make smarter, data-driven lending decisions.

📌 Problem Statement

Loan defaults cause significant financial losses for banks and lending institutions.
Traditional rule-based credit evaluation systems struggle with:

Large-scale datasets

Class imbalance

Complex customer behavior patterns

This project addresses these challenges using a robust end-to-end machine learning pipeline focused on risk minimization.

💡 Solution Overview

We built a complete credit risk prediction system that:

Ingests and stores raw credit data

Performs in-depth Exploratory Data Analysis (EDA)

Applies advanced feature engineering

Trains and evaluates multiple classification models

Prioritizes Recall to reduce false negatives (high-risk customers classified as low-risk)

🧰 Tech Stack
Category	Tools
Data Source	Kaggle
Database	MongoDB
Notebook	Google Colab
Language	Python
Libraries	pandas, numpy, scikit-learn, seaborn, matplotlib, pymongo
Visualisations  Dynamic dashboard using streamlit.
🔄 Project Workflow
Data Collection (Kaggle)
        ↓
Raw Data Storage (MongoDB)
        ↓
Data Extraction (MongoDB → Colab)
        ↓
Data Validation & Sanity Checks
        ↓
Exploratory Data Analysis (EDA)
        ↓
Data Cleaning & Preprocessing
        ↓
Feature Engineering
        ↓
Refined Data Storage (MongoDB)
        ↓
Train–Test Split
        ↓
Feature Encoding
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Hyperparameter Tuning
        ↓
Final Evaluation & Visualization

📊 Evaluation Metrics

Due to class imbalance, we focused on metrics that matter most in credit risk modeling:

Recall (Primary metric – minimize false negatives)

Precision

F1-Score

ROC–AUC

📈 Key Visualizations

ROC Curve

KS Statistic

Feature Importance

Model Performance Comparison


Made a dynamic dashboard using streamlit wherein different categorical columns are checked against the default


