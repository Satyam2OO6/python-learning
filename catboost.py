from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Dataset
data = pd.DataFrame({
    "Age": [22,25,30,45,50,55],
    "Gender": ["Male","Female","Male","Male","Female","Male"],
    "City": ["Delhi","Mumbai","Delhi","Kolkata","Mumbai","Delhi"],
    "Bought": [0,0,0,1,1,1]
})

X = data[["Age","Gender","City"]]
y = data["Bought"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Categorical column indices
cat_features = [1,2]

# Create model
model = CatBoostClassifier(
    iterations=100,
    learning_rate=0.1,
    depth=3,
    verbose=0
)

# Train
model.fit(
    X_train,
    y_train,
    cat_features=cat_features
)

# Predict
predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))