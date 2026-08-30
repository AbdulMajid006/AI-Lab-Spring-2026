import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

np.random.seed(42)
n = 200

data = pd.DataFrame({
    'study_hours':       np.random.uniform(1, 10, n).round(1),
    'attendance':        np.random.uniform(50, 100, n).round(1),   # % attendance
    'previous_grade':    np.random.uniform(40, 95, n).round(1),
    'participation':     np.random.choice(['Low', 'Medium', 'High'], n),
    'internet_usage':    np.random.uniform(1, 8, n).round(1),       # hours/day
})

data.loc[np.random.choice(n, 15, replace=False), 'attendance']     = np.nan
data.loc[np.random.choice(n, 10, replace=False), 'study_hours']    = np.nan
data.loc[np.random.choice(n, 8,  replace=False), 'previous_grade'] = np.nan

data['final_score'] = (
    0.40 * data['study_hours'].fillna(data['study_hours'].median()) * 5 +
    0.25 * data['attendance'].fillna(data['attendance'].median()) * 0.6 +
    0.20 * data['previous_grade'].fillna(data['previous_grade'].median()) * 0.7 +
    0.10 * data['internet_usage'] * (-1.5) +
    np.random.normal(0, 3, n)
).clip(0, 100).round(2)

print("=" * 55)
print("         STUDENT PERFORMANCE PREDICTION")
print("=" * 55)

print("\n[1] Raw Dataset (first 5 rows):")
print(data.head())

print("\n[2] Missing Values:")
print(data.isnull().sum())

data['study_hours']    = data['study_hours'].fillna(data['study_hours'].median())
data['attendance']     = data['attendance'].fillna(data['attendance'].median())
data['previous_grade'] = data['previous_grade'].fillna(data['previous_grade'].median())

print("\n[3] Missing Values After Cleaning:")
print(data.isnull().sum())

le = LabelEncoder()
data['participation_encoded'] = le.fit_transform(data['participation'])

participation_map = {'Low': 0, 'Medium': 1, 'High': 2}
data['participation_encoded'] = data['participation'].map(participation_map)

print("\n[4] Participation Encoding (Low=0, Medium=1, High=2):")
print(data[['participation', 'participation_encoded']].drop_duplicates().sort_values('participation_encoded'))

features = ['study_hours', 'attendance', 'previous_grade',
            'participation_encoded', 'internet_usage']
X = data[features]
y = data['final_score']

print("\n[5] Feature Correlations with Final Score:")
corr = data[features + ['final_score']].corr()['final_score'].drop('final_score').sort_values(ascending=False)
print(corr.round(3))

plt.figure(figsize=(8, 5))
sns.heatmap(data[features + ['final_score']].corr(), annot=True, fmt='.2f',
            cmap='coolwarm', linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=100)
plt.close()
print("\n   >> Correlation heatmap saved as 'correlation_heatmap.png'")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\n[6] Train size: {len(X_train)} | Test size: {len(X_test)}")

LR = LinearRegression()
LR.fit(X_train, y_train)
pred_LR = LR.predict(X_test)

DT = DecisionTreeRegressor(max_depth=5, random_state=42)
DT.fit(X_train, y_train)
pred_DT = DT.predict(X_test)

def evaluate(name, y_true, y_pred):
    mae  = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2   = r2_score(y_true, y_pred)
    print(f"\n  {name}")
    print(f"    MAE  (Mean Absolute Error)       : {mae:.4f}")
    print(f"    RMSE (Root Mean Squared Error)   : {rmse:.4f}")
    print(f"    R²   (Coefficient of Determination): {r2:.4f} ({r2*100:.2f}%)")

print("\n[7] Model Evaluation on Test Set:")
print("-" * 50)
evaluate("Linear Regression", y_test, pred_LR)
evaluate("Decision Tree Regressor (max_depth=5)", y_test, pred_DT)

# Feature Importance from Decision Tree
print("\n[8] Feature Importance (Decision Tree):")
importance_df = pd.DataFrame({
    'Feature': features,
    'Importance': DT.feature_importances_
}).sort_values('Importance', ascending=False)
print(importance_df.to_string(index=False))

print("\n" + "=" * 55)
print("       PREDICTING FINAL SCORE FOR A NEW STUDENT")
print("=" * 55)

new_student = pd.DataFrame({
    'study_hours':           [7.5],
    'attendance':            [85.0],
    'previous_grade':        [78.0],
    'participation_encoded': [2],    # High
    'internet_usage':        [3.0],
})

print("\nNew Student Features:")
print(f"  Study Hours       : {new_student['study_hours'][0]} hrs/day")
print(f"  Attendance        : {new_student['attendance'][0]}%")
print(f"  Previous Grade    : {new_student['previous_grade'][0]}")
print(f"  Participation     : High (encoded=2)")
print(f"  Internet Usage    : {new_student['internet_usage'][0]} hrs/day")

pred_new_LR = LR.predict(new_student)[0]
pred_new_DT = DT.predict(new_student)[0]

print(f"\n  Predicted Final Score (Linear Regression)   : {pred_new_LR:.2f} / 100")
print(f"  Predicted Final Score (Decision Tree)       : {pred_new_DT:.2f} / 100")

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.scatter(y_test, pred_LR, alpha=0.6, color='steelblue', edgecolors='k', s=40)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel("Actual Score")
plt.ylabel("Predicted Score")
plt.title("Linear Regression\nActual vs Predicted")

plt.subplot(1, 2, 2)
plt.scatter(y_test, pred_DT, alpha=0.6, color='darkorange', edgecolors='k', s=40)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel("Actual Score")
plt.ylabel("Predicted Score")
plt.title("Decision Tree Regressor\nActual vs Predicted")

plt.tight_layout()
plt.savefig('actual_vs_predicted.png', dpi=100)
plt.close()
print("\n   >> Actual vs Predicted plot saved as 'actual_vs_predicted.png'")

print("\n" + "=" * 55)
print("                   DONE!")
print("=" * 55)