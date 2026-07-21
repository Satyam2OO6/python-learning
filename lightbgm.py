from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Features
X = [
    [22,25000],
    [25,30000],
    [30,40000],
    [45,80000],
    [50,90000],
    [55,100000],
    [27,35000],
    [47,85000]
]

# Labels
y = [0,0,0,1,1,1,0,1]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# Create model
model = LGBMClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

# Predict a new customer
customer = [[35,60000]]
print("Prediction:", model.predict(customer))