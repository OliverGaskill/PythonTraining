# Iris Flower Classification with Decision Tree

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# ------------------------
# Step 1: Load Dataset
# ------------------------
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add species column (numeric targets)
df["species"] = iris.target

# Map numbers to names
df["species"] = df["species"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

print("First 5 rows of dataset:")
print(df.head())

# ------------------------
# Step 2: Split Data
# ------------------------
X = df[iris.feature_names]   # Features (flower measurements)
y = df["species"]            # Labels (flower species)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTraining samples: {len(X_train)}, Test samples: {len(X_test)}")

# ------------------------
# Step 3: Train Model
# ------------------------
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# ------------------------
# Step 4: Evaluate Model
# ------------------------
y_pred = model.predict(X_test)

print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ------------------------
# Step 5: Predict New Flower
# ------------------------
# Example: sepal length=5.1, sepal width=3.5, petal length=1.4, petal width=0.2
new_flower = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(new_flower)

print("\nPrediction for new flower:", prediction[0])
