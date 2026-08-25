from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Create sample data
X, y = make_blobs(
    n_samples=300,
    centers=4,
    cluster_std=1.0,
    random_state=42
)

# Create K-Means model
kmeans = KMeans(
    n_clusters=4,
    random_state=42
)

# Train model
kmeans.fit(X)

# Predict clusters
labels = kmeans.predict(X)

# Cluster centers
centers = kmeans.cluster_centers_

# Plot
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=labels
)

plt.scatter(
    centers[:, 0],
    centers[:, 1],
    marker="X",
    s=200
)

plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()