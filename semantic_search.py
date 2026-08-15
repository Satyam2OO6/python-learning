from sentence_transformers import SentenceTransformer, util

# Load a pre-trained sentence embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Documents
documents = [
    "Python is a programming language.",
    "Machine learning allows computers to learn from data.",
    "Deep learning uses neural networks.",
    "Football is a popular sport."
]

# User query
query = "How do computers learn from data?"

# Convert documents and query into embeddings
document_embeddings = model.encode(documents, convert_to_tensor=True)
query_embedding = model.encode(query, convert_to_tensor=True)

# Calculate similarity
scores = util.cos_sim(query_embedding, document_embeddings)[0]

# Find most similar document
best_index = scores.argmax().item()

print("Query:", query)
print("\nMost Similar Document:")
print(documents[best_index])
print("\nSimilarity Score:", round(scores[best_index].item(), 3))