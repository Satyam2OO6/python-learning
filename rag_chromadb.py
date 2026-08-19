import chromadb
from sentence_transformers import SentenceTransformer

# -----------------------------
# 1. Create ChromaDB
# -----------------------------
client = chromadb.Client()

collection = client.create_collection(
    name="ml_knowledge"
)

# -----------------------------
# 2. Documents
# -----------------------------
documents = [
    "Python is a programming language.",
    "Machine learning allows computers to learn from data.",
    "Deep learning uses neural networks with multiple layers.",
    "CNNs are commonly used for image classification.",
    "RNNs are useful for sequential data.",
    "Transformers use attention mechanisms."
]

# -----------------------------
# 3. Load Embedding Model
# -----------------------------
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

embeddings = model.encode(
    documents
).tolist()

# -----------------------------
# 4. Store Documents
# -----------------------------
collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(documents))]
)

# -----------------------------
# 5. User Query
# -----------------------------
query = input("Enter your question: ")

query_embedding = model.encode(
    [query]
).tolist()

# -----------------------------
# 6. Search ChromaDB
# -----------------------------
results = collection.query(
    query_embeddings=query_embedding,
    n_results=3
)

# -----------------------------
# 7. Display Results
# -----------------------------
print("\nRelevant Documents:\n")

for document in results["documents"][0]:
    print("-", document)