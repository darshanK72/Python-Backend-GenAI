# 01 — scikit-learn introduction
# Notebook (recommended): 01-sklearn.ipynb
# Run: python 01_sklearn_intro.py

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# --- 1. Load built-in dataset ---
iris = load_iris()
X, y = iris.data, iris.target
print("samples:", X.shape[0], "features:", X.shape[1])
print("target names:", iris.target_names)

# --- 2. Train/test split ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# --- 3. Fit model ---
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# --- 4. Predict and evaluate ---
preds = model.predict(X_test)
print("accuracy:", accuracy_score(y_test, preds))
