from sklearn.naive_bayes import GaussianNB

# Features
X = [
    [150,7],
    [170,8],
    [140,6],
    [130,5],
    [120,4],
    [110,4]
]

# Labels
y = [
    "Apple",
    "Apple",
    "Apple",
    "Orange",
    "Orange",
    "Orange"
]

# Create model
model = GaussianNB()

# Train model
model.fit(X, y)

# Predict
fruit = [[145,6]]

prediction = model.predict(fruit)

print("Prediction:", prediction[0])