from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# -----------------------------
# 1. Documents
# -----------------------------
documents = [
    "Python is a programming language.",
    "Machine learning allows computers to learn from data.",
    "Deep learning uses neural networks.",
    "CNNs are mainly used for image processing.",
    "RNNs are useful for sequential data.",
    "Transformers use attention mechanisms."
]

# -----------------------------
# 2. Load Embedding Model
# -----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(documents)

# Convert to NumPy float32
embeddings = np.array(
    embeddings,
    dtype="float32"
)

# -----------------------------
# 3. Create FAISS Index
# -----------------------------
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# -----------------------------
# 4. User Query
# -----------------------------
query = input("Enter your question: ")

query_embedding = model.encode([query])

query_embedding = np.array(
    query_embedding,
    dtype="float32"
)

# -----------------------------
# 5. Search
# -----------------------------
k = 2

distances, indices = index.search(
    query_embedding,
    k
)

# -----------------------------
# 6. Display Results
# -----------------------------
print("\nMost Relevant Documents:\n")

for i in indices[0]:
    print("-", documents[i])