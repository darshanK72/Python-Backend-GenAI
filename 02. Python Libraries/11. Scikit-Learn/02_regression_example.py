# 02 — Linear regression example
# Run: python 02_regression_example.py

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# hours studied vs exam score (synthetic)
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([55, 62, 68, 74, 80, 88])

model = LinearRegression()
model.fit(X, y)

pred = model.predict([[3.5]])[0]
print(f"predicted score for 3.5 hours: {pred:.1f}")
print("slope:", model.coef_[0], "intercept:", model.intercept_)

y_pred = model.predict(X)
print("MSE:", mean_squared_error(y, y_pred))
print("R2:", r2_score(y, y_pred))
