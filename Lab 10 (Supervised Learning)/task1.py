Student Performance Prediction
You are working as a data scientist for a university. Your goal is to predict a student’s final exam
score (continuous variable) based on various factors such as study hours, attendance, previous
grades, participation in class, and internet usage.
Perform the following tasks:
 Clean the dataset and handle missing values (e.g., missing attendance or study hours).
 Encode categorical variables (e.g., participation level: Low, Medium, High).
 Identify the most important features affecting student performance.
 Train a regression model to predict the final score.
 Evaluate the model using appropriate metrics (e.g., MAE, RMSE, R2).
 Predict the final score for a new student given their features.


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = {
    "Study_Hours": [5, 8, 6, 7, np.nan, 4, 9, 10, 3, 6],
    "Attendance": [85, 90, np.nan, 88, 92, 75, 95, 98, 70, 80],
    "Previous_Grades": [78, 85, 80, 82, 88, 70, 91, 95, 65, 79],
    "Participation_Level": ["High", "Medium", "High", "Low", "Medium", "Low", "High", "High", "Low", "Medium"],
    "Internet_Usage": [3, 5, 4, 2, 6, 1, 5, 6, 2, 3],
    "Final_Score": [80, 88, 84, 79, 90, 68, 94, 97, 60, 81]
}

df = pd.DataFrame(data)

df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

le = LabelEncoder()
df["Participation_Level"] = le.fit_transform(df["Participation_Level"])

X = df.drop("Final_Score", axis=1)
y = df["Final_Score"]

print("Feature Importance Based on Correlation:")
print(df.corr()["Final_Score"].sort_values(ascending=False))

x_train, x_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

LR = LinearRegression()

ModelLR = LR.fit(x_train, y_train)

PredictionLR = ModelLR.predict(x_test)

print("\nPredictions:")
print(PredictionLR)

mae = mean_absolute_error(y_test, PredictionLR)
rmse = np.sqrt(mean_squared_error(y_test, PredictionLR))
r2 = r2_score(y_test, PredictionLR)

print("\nModel Evaluation")
print("MAE:", mae)
print("RMSE:", rmse)

print("LR Testing Accuracy")
testingAccLR = r2 * 100
print(testingAccLR)

new_student = pd.DataFrame({
    "Study_Hours": [7],
    "Attendance": [89],
    "Previous_Grades": [84],
    "Participation_Level": [2],
    "Internet_Usage": [4]
})

predicted_score = ModelLR.predict(new_student)

print("\nPredicted Final Score for New Student:")
print(predicted_score[0])
