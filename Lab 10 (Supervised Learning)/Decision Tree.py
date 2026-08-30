from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Initialize the DecisionTreeClassifier
DT = DecisionTreeClassifier()

# Train the model
ModelDT = DT.fit(x_train, y_train)

# Model Testing (Prediction)
PredictionDT = DT.predict(x_test)
print("Predictions:", PredictionDT)

# Model Training Accuracy
print('DT Training Accuracy')
tracDT = DT.score(x_train, y_train) # The score method gives accuracy
directly

TrainingAccDT = tracDT * 100
print(f"Training Accuracy: {TrainingAccDT:.2f}%")

# Model Testing Accuracy
print('DT Testing Accuracy')
teacDT = accuracy_score(y_test, PredictionDT)
testingAccDT = teacDT * 100
print(f"Testing Accuracy: {testingAccDT:.2f}%")
