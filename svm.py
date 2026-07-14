from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Features
X = [
    [22,25000],
    [25,30000],
    [47,50000],
    [52,110000],
    [46,90000],
    [56,120000],
    [27,35000],
    [30,40000],
    [48,100000],
    [50,105000]
]

# Labels
y = [0,0,1,1,1,1,0,0,1,1]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = SVC(kernel="linear")

# Train
model.fit(X_train, y_train)

# Predict
prediction = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, prediction))

# Predict new customer
customer = [[35,60000]]

print(model.predict(customer))