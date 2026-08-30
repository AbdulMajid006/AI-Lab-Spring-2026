# Task#2:
# Loan Approval Classification:
# You are working for a bank to automate loan approvals. The dataset contains customer details
# such as income, employment status, credit score, loan amount, and marital status. The goal is to
# classify whether a loan should be approved (1) or rejected (0).
# Perform the following tasks:
# • Preprocess the dataset:
#     o Handle missing values
#     o Encode categorical variables (e.g., employment status, marital status)
# • Perform feature selection to identify key factors influencing loan approval
# • Train a classification model (e.g., Logistic Regression, Decision Tree)
# • Split the dataset into training and testing sets
# • Evaluate the model using metrics like accuracy, precision, recall, and F1-score
# • Use the model to predict loan approval for a new applicant


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

data = {
    "Income": [50000, 60000, np.nan, 80000, 30000, 45000, 70000, 90000, 35000, 40000],
    "Employment_Status": ["Employed", "Self-Employed", "Employed", "Unemployed", "Employed", "Self-Employed", "Employed", "Employed", "Unemployed", "Employed"],
    "Credit_Score": [700, 650, 720, 580, 600, 680, 750, 800, 590, np.nan],
    "Loan_Amount": [20000, 25000, 15000, 30000, 10000, 18000, 22000, 27000, 12000, 16000],
    "Marital_Status": ["Married", "Single", "Married", "Single", "Married", "Single", "Married", "Married", "Single", "Married"],
    "Loan_Approved": [1, 1, 1, 0, 0, 1, 1, 1, 0, 0]
}

df = pd.DataFrame(data)

df["Income"] = df["Income"].fillna(df["Income"].mean())
df["Credit_Score"] = df["Credit_Score"].fillna(df["Credit_Score"].mean())

le1 = LabelEncoder()
le2 = LabelEncoder()

df["Employment_Status"] = le1.fit_transform(df["Employment_Status"])
df["Marital_Status"] = le2.fit_transform(df["Marital_Status"])

X = df.drop("Loan_Approved", axis=1)
y = df["Loan_Approved"]

print("Feature Correlation with Target:")
print(df.corr()["Loan_Approved"].sort_values(ascending=False))

x_train, x_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier()

model.fit(x_train, y_train)

prediction = model.predict(x_test)

print("\nPredictions:")
print(prediction)

accuracy = accuracy_score(y_test, prediction) * 100
precision = precision_score(y_test, prediction) * 100
recall = recall_score(y_test, prediction) * 100
f1 = f1_score(y_test, prediction) * 100

print("\nModel Evaluation")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

new_applicant = pd.DataFrame({
    "Income": [55000],
    "Employment_Status": [1],
    "Credit_Score": [710],
    "Loan_Amount": [20000],
    "Marital_Status": [0]
})

result = model.predict(new_applicant)

print("\nLoan Approval Prediction for New Applicant:")
print(result[0])
