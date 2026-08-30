import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

data = {
    "Monthly_Charges": [70, 80, 65, 90, 50, 60, 85, 95, 55, 75],
    "Contract_Type": ["Month-to-Month", "One Year", "Month-to-Month", "Two Year", "Month-to-Month", "One Year", "Two Year", "Two Year", "Month-to-Month", "One Year"],
    "Tenure": [1, 24, 3, 36, 2, 12, 48, 60, 4, 18],
    "Internet_Service": ["Fiber", "DSL", "Fiber", "Fiber", "DSL", "DSL", "Fiber", "Fiber", "DSL", "DSL"],
    "Support_Calls": [5, 2, 6, 1, 7, 3, 2, 1, 6, 4],
    "Churn": [1, 0, 1, 0, 1, 0, 0, 0, 1, 0]
}

df = pd.DataFrame(data)

df["Monthly_Charges"] = df["Monthly_Charges"].fillna(df["Monthly_Charges"].mean())
df["Tenure"] = df["Tenure"].fillna(df["Tenure"].mean())
df["Support_Calls"] = df["Support_Calls"].fillna(df["Support_Calls"].mean())

le1 = LabelEncoder()
le2 = LabelEncoder()

df["Contract_Type"] = le1.fit_transform(df["Contract_Type"])
df["Internet_Service"] = le2.fit_transform(df["Internet_Service"])

Q1 = df["Monthly_Charges"].quantile(0.25)
Q3 = df["Monthly_Charges"].quantile(0.75)
IQR = Q3 - Q1

df = df[(df["Monthly_Charges"] >= Q1 - 1.5 * IQR) & (df["Monthly_Charges"] <= Q3 + 1.5 * IQR)]

X = df.drop("Churn", axis=1)
y = df["Churn"]

scaler = StandardScaler()
X = scaler.fit_transform(X)

print("Feature Importance (Approx using correlation):")
print(df.corr()["Churn"].sort_values(ascending=False))

x_train, x_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = SVC(kernel="linear")

model.fit(x_train, y_train)

prediction = model.predict(x_test)

print("\nPredictions:")
print(prediction)

cm = confusion_matrix(y_test, prediction)
accuracy = accuracy_score(y_test, prediction) * 100
precision = precision_score(y_test, prediction) * 100
recall = recall_score(y_test, prediction) * 100
f1 = f1_score(y_test, prediction) * 100

print("\nConfusion Matrix:")
print(cm)

print("\nModel Evaluation")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

new_customer = pd.DataFrame({
    "Monthly_Charges": [78],
    "Contract_Type": [1],
    "Tenure": [10],
    "Internet_Service": [0],
    "Support_Calls": [4]
})

new_customer = scaler.transform(new_customer)

result = model.predict(new_customer)

print("\nChurn Prediction for New Customer:")
print(result[0])