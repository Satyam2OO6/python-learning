from sklearn.neighbors import KNeighborsClassifier

# Features
X = [
    [150,45],
    [155,48],
    [160,50],
    [170,70],
    [175,75],
    [180,80]
]

# Labels
y = [
    "Football",
    "Football",
    "Football",
    "Basketball",
    "Basketball",
    "Basketball"
]

# Create KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Train model
model.fit(X, y)

# Predict
person = [[165,60]]

prediction = model.predict(person)

print("Prediction:", prediction[0])