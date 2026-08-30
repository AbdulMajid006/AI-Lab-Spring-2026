import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score,
                             confusion_matrix, classification_report)

np.random.seed(42)
n = 300

employment_status = np.random.choice(['Employed', 'Self-Employed', 'Unemployed'], n,
                                      p=[0.55, 0.30, 0.15])
marital_status    = np.random.choice(['Single', 'Married', 'Divorced'], n,
                                      p=[0.40, 0.45, 0.15])
income            = np.random.randint(20000, 150000, n)
credit_score      = np.random.randint(300, 850, n)
loan_amount       = np.random.randint(5000, 80000, n)

approved = (
    (credit_score > 600).astype(int) +
    (income > 50000).astype(int) +
    (employment_status != 'Unemployed').astype(int) +
    (loan_amount < 40000).astype(int)
)
loan_approved = (approved >= 3).astype(int)

data = pd.DataFrame({
    'income':            income,
    'employment_status': employment_status,
    'credit_score':      credit_score,
    'loan_amount':       loan_amount,
    'marital_status':    marital_status,
    'loan_approved':     loan_approved
})

data.loc[np.random.choice(n, 20, replace=False), 'credit_score']      = np.nan
data.loc[np.random.choice(n, 15, replace=False), 'income']            = np.nan
data.loc[np.random.choice(n, 10, replace=False), 'employment_status'] = np.nan
data.loc[np.random.choice(n, 8,  replace=False), 'marital_status']    = np.nan

print("=" * 58)
print("          LOAN APPROVAL CLASSIFICATION")
print("=" * 58)

print("\n[1] Raw Dataset (first 5 rows):")
print(data.head().to_string())

print(f"\n[2] Dataset Shape: {data.shape[0]} rows x {data.shape[1]} columns")

print("\n[3] Class Distribution:")
vc = data['loan_approved'].value_counts()
print(f"    Approved (1) : {vc.get(1, 0)}  |  Rejected (0) : {vc.get(0, 0)}")

print("\n[4] Missing Values Before Cleaning:")
print(data.isnull().sum().to_string())

data['credit_score'] = data['credit_score'].fillna(data['credit_score'].median())
data['income']       = data['income'].fillna(data['income'].median())

# Categorical columns → fill with mode
data['employment_status'] = data['employment_status'].fillna(
    data['employment_status'].mode()[0])
data['marital_status']    = data['marital_status'].fillna(
    data['marital_status'].mode()[0])

print("\n[5] Missing Values After Cleaning:")
print(data.isnull().sum().to_string())

le_emp     = LabelEncoder()
le_marital = LabelEncoder()

data['employment_encoded'] = le_emp.fit_transform(data['employment_status'])
data['marital_encoded']    = le_marital.fit_transform(data['marital_status'])

print("\n[6] Encoding Maps:")
print("    Employment Status →",
      dict(zip(le_emp.classes_, le_emp.transform(le_emp.classes_))))
print("    Marital Status    →",
      dict(zip(le_marital.classes_, le_marital.transform(le_marital.classes_))))

features = ['income', 'credit_score', 'loan_amount',
            'employment_encoded', 'marital_encoded']
X = data[features]
y = data['loan_approved']

print("\n[7] Feature Correlations with Loan Approval:")
corr = data[features + ['loan_approved']].corr()['loan_approved'].drop('loan_approved')
print(corr.sort_values(ascending=False).round(3).to_string())

plt.figure(figsize=(8, 5))
sns.heatmap(data[features + ['loan_approved']].corr(),
            annot=True, fmt='.2f', cmap='RdYlGn', linewidths=0.5)
plt.title("Feature Correlation Heatmap — Loan Approval")
plt.tight_layout()
plt.savefig('loan_correlation_heatmap.png', dpi=100)
plt.close()
print("\n   >> Heatmap saved as 'loan_correlation_heatmap.png'")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"\n[8] Train size: {len(X_train)} | Test size: {len(X_test)}")

scaler   = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc  = scaler.transform(X_test)

LR = LogisticRegression(max_iter=1000, random_state=42)
LR.fit(X_train_sc, y_train)
pred_LR = LR.predict(X_test_sc)

DT = DecisionTreeClassifier(max_depth=5, random_state=42)
DT.fit(X_train, y_train)
pred_DT = DT.predict(X_test)

def evaluate_classifier(name, y_true, y_pred):
    acc  = accuracy_score(y_true, y_pred)  * 100
    prec = precision_score(y_true, y_pred, zero_division=0) * 100
    rec  = recall_score(y_true, y_pred,    zero_division=0) * 100
    f1   = f1_score(y_true, y_pred,        zero_division=0) * 100
    print(f"\n  {'─'*46}")
    print(f"  {name}")
    print(f"  {'─'*46}")
    print(f"    Accuracy  : {acc:.2f}%")
    print(f"    Precision : {prec:.2f}%")
    print(f"    Recall    : {rec:.2f}%")
    print(f"    F1-Score  : {f1:.2f}%")
    print(f"\n  Classification Report:\n")
    print(classification_report(y_true, y_pred,
          target_names=['Rejected (0)', 'Approved (1)'],
          zero_division=0))

print("\n[9] Model Evaluation:")
evaluate_classifier("Logistic Regression", y_test, pred_LR)
evaluate_classifier("Decision Tree Classifier (max_depth=5)", y_test, pred_DT)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
models     = [("Logistic Regression", pred_LR),
              ("Decision Tree", pred_DT)]
colors     = ['Blues', 'Oranges']

for ax, (name, pred), cmap in zip(axes, models, colors):
    cm = confusion_matrix(y_test, pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap=cmap, ax=ax,
                xticklabels=['Rejected', 'Approved'],
                yticklabels=['Rejected', 'Approved'])
    ax.set_title(f"{name}\nConfusion Matrix")
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")

plt.tight_layout()
plt.savefig('loan_confusion_matrices.png', dpi=100)
plt.close()
print("   >> Confusion matrices saved as 'loan_confusion_matrices.png'")

print("\n[10] Feature Importance (Decision Tree):")
imp_df = pd.DataFrame({
    'Feature':    features,
    'Importance': DT.feature_importances_
}).sort_values('Importance', ascending=False)
print(imp_df.to_string(index=False))

print("\n" + "=" * 58)
print("        PREDICTING LOAN APPROVAL FOR NEW APPLICANT")
print("=" * 58)

# Encode the new applicant's categorical values using fitted encoders
new_employment = le_emp.transform(['Employed'])[0]
new_marital    = le_marital.transform(['Married'])[0]

new_applicant = pd.DataFrame({
    'income':             [75000],
    'credit_score':       [720],
    'loan_amount':        [25000],
    'employment_encoded': [new_employment],
    'marital_encoded':    [new_marital],
})

print("\nNew Applicant Details:")
print(f"  Income            : Rs. 75,000")
print(f"  Credit Score      : 720")
print(f"  Loan Amount       : Rs. 25,000")
print(f"  Employment Status : Employed")
print(f"  Marital Status    : Married")

new_scaled = scaler.transform(new_applicant)

pred_new_LR = LR.predict(new_scaled)[0]
prob_new_LR = LR.predict_proba(new_scaled)[0]

pred_new_DT = DT.predict(new_applicant)[0]
prob_new_DT = DT.predict_proba(new_applicant)[0]

def verdict(p): return "✅ APPROVED" if p == 1 else "❌ REJECTED"

print(f"\n  Logistic Regression  → {verdict(pred_new_LR)}")
print(f"    Approval Probability : {prob_new_LR[1]*100:.1f}%")
print(f"    Rejection Probability: {prob_new_LR[0]*100:.1f}%")

print(f"\n  Decision Tree        → {verdict(pred_new_DT)}")
print(f"    Approval Probability : {prob_new_DT[1]*100:.1f}%")
print(f"    Rejection Probability: {prob_new_DT[0]*100:.1f}%")

print("\n" + "=" * 58)
print("                       DONE!")
print("=" * 58)