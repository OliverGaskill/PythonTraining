from traceback import print_tb

import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt


housing = fetch_california_housing()

df = pd.DataFrame(housing.data, columns=housing.feature_names)
df["target"] = housing.target

print("First 5 rows of dataset: ")
print(df.head())


x = df[housing.feature_names]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

print(f"\nTraining samples: {len(X_train)}, Test samples: {len(X_test)}")


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.2f}")

plt.figure(figsize=(8,6))
plt.scatter(df["MedInc"], df["target"], alpha=0.3)
plt.xlabel("Median Income (10,000s of $)")
plt.ylabel("House Price (100,000s of $)")
plt.title("Median Income vs House Price")
plt.show()

new_house = pd.DataFrame([[8.3, 20, 6.5, 1.0, 1500, 3.0, 34.2, -118.4]],
                         columns=housing.feature_names)

prediction = model.predict(new_house)
print(f"\nPredicted House Price: ${prediction[0]*100000:.2f}")

# Compare Actual vs Predicted ----------------------------------------

import matplotlib.pyplot as plt
import numpy as np

X_income = X_test["MedInc"]
y_actual = y_test
y_pred = model.predict(X_test)

# Scatter of actual prices
plt.figure(figsize=(8,6))
plt.scatter(X_income, y_actual, alpha=0.3, label="Actual Prices")

# Line of predicted prices
sorted_idx = np.argsort(X_income)
plt.plot(X_income.iloc[sorted_idx], y_pred[sorted_idx], color="red", linewidth=2, label="Model Prediction")

plt.xlabel("Median Income (10,000s of $)")
plt.ylabel("House Price (100,000s of $)")
plt.title("Actual vs Predicted House Prices")
plt.legend()

plt.savefig("house_prices.png", dpi=300)  # saves in your project folder
plt.show()





housing = fetch_california_housing()
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df["target"] = housing.target

X = df[housing.feature_names]
y = df["target"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Random Forest Model Performance:")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.2f}")

new_house = pd.DataFrame([[8.3, 20, 6.5, 1.0, 1500, 3.0, 34.2, -118.4]],
                         columns=housing.feature_names)
prediction = model.predict(new_house)
print(f"\nPredicted House Price: ${prediction[0]*100000:.2f}")

X_income = X_test["MedInc"]
y_actual = y_test
y_pred_sorted = model.predict(X_test)

plt.figure(figsize=(8,6))
plt.scatter(X_income, y_actual, alpha=0.3, label="Actual Prices")
sorted_idx = np.argsort(X_income)
plt.plot(X_income.iloc[sorted_idx], y_pred_sorted[sorted_idx], color="red", linewidth=2, label="Model Prediction")
plt.xlabel("Median Income (10,000s of $)")
plt.ylabel("House Price (100,000s of $)")
plt.title("Actual vs Predicted House Prices (Random Forest)")
plt.legend()
plt.savefig("house_prices_random_forest.png", dpi=300, bbox_inches="tight")
plt.show()














