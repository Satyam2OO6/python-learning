from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel
from sklearn.metrics import mean_squared_error, r2_score

data = load_diabetes()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

kernel = ConstantKernel(1.0) * RBF(1.0)

model = GaussianProcessRegressor(
    kernel=kernel,
    random_state=42
)

model.fit(X_train, y_train)

y_pred, uncertainty = model.predict(
    X_test,
    return_std=True
)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R2 Score:", r2)

prediction, std = model.predict(
    [X_test[0]],
    return_std=True
)

print("\nActual Value:", y_test[0])
print("Predicted Value:", prediction[0])
print("Prediction Uncertainty:", std[0])