from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Features
X = [
    [22,25000],
    [25,27000],
    [26,30000],
    [45,80000],
    [47,85000],
    [50,90000],
    [28,32000],
    [48,88000]
]

# Create model
model = KMeans(n_clusters=2, random_state=42)

# Train model
model.fit(X)

# Cluster labels
print(model.labels_)

# Cluster centers
print(model.cluster_centers_)

# Plot
ages = [x[0] for x in X]
income = [x[1] for x in X]

plt.scatter(ages, income, c=model.labels_, s=100)
plt.scatter(
    model.cluster_centers_[:,0],
    model.cluster_centers_[:,1],
    marker="X",
    s=250
)

plt.xlabel("Age")
plt.ylabel("Income")
plt.title("K-Means Clustering")
plt.show()