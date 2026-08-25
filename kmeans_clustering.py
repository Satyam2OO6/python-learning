from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Create sample data
X, y = make_blobs(
    n_samples=300,
    centers=3,
    cluster_std=1.0,
    random_state=42
)

# Create K-Means model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Train model
model.fit(X)

# Get cluster labels
labels = model.labels_

# Get cluster centers
centers = model.cluster_centers_

# Display cluster information
print("Cluster Labels:")
print(labels)

print("\nCluster Centers:")
print(centers)

# Visualize clusters
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