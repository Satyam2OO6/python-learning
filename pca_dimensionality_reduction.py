from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load Iris dataset
data = load_iris()

X = data.data
y = data.target

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create PCA model
pca = PCA(n_components=2)

# Reduce dimensions
X_pca = pca.fit_transform(X_scaled)

# Display explained variance
print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)

# Visualize reduced data
plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=y
)

plt.title("PCA Dimensionality Reduction")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.show()