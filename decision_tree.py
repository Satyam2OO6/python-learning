from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

# Features
X = [
    [22, 25000],
    [25, 30000],
    [47, 50000],
    [52, 110000],
    [46, 90000],
    [56, 120000],
    [27, 35000],
    [30, 40000],
    [48, 100000],
    [50, 105000]
]

# Labels
y = [0, 0, 1, 1, 1, 1, 0, 0, 1, 1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict a new person
new_person = [[35, 60000]]
prediction = model.predict(new_person)

print("Prediction:", prediction)

# Visualize the tree
plt.figure(figsize=(10, 6))
tree.plot_tree(
    model,
    feature_names=["Age", "Salary"],
    class_names=["No", "Yes"],
    filled=True
)
plt.show()