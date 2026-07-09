from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample data: House size (sq ft) and price
X = [[1000], [1500], [2000], [2500], [3000]]
y = [200000, 300000, 400000, 500000, 600000]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

# Predict price for a new house
new_house = [[1800]]
predicted_price = model.predict(new_house)

print("Predicted price:", predicted_price[0])