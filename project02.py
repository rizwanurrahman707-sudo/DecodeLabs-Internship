import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
data = pd.read_csv("heart.csv")

# Features and Target
X = data.drop("target", axis=1)
y = data["target"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, prediction)

print("Heart Disease Prediction Model")
print("Model Accuracy:", accuracy)

for i in range(5):
    print(
        "Actual:", y_test.iloc[i],
        "Predicted:", prediction[i]
    )
    