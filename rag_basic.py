from sentence_transformers import SentenceTransformer, util
from transformers import pipeline

# -----------------------------
# 1. Knowledge Base
# -----------------------------
documents = [
    "Python is a programming language used for software development.",
    "Machine learning allows computers to learn patterns from data.",
    "Deep learning uses neural networks with multiple layers.",
    "CNNs are commonly used for image classification.",
    "RNNs are designed to work with sequential data."
]

# -----------------------------
# 2. Load Embedding Model
# -----------------------------
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Create document embeddings
document_embeddings = embedding_model.encode(
    documents,
    convert_to_tensor=True
)

# -----------------------------
# 3. User Question
# -----------------------------
question = "What is machine learning?"

# Convert question to embedding
question_embedding = embedding_model.encode(
    question,
    convert_to_tensor=True
)

# -----------------------------
# 4. Find Relevant Document
# -----------------------------
scores = util.cos_sim(
    question_embedding,
    document_embeddings
)[0]

best_index = scores.argmax().item()

context = documents[best_index]

# -----------------------------
# 5. Generate Answer
# -----------------------------
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}

Answer:
"""

result = generator(
    prompt,
    max_new_tokens=50
)

# -----------------------------
# 6. Display Result
# -----------------------------
print("Question:")
print(question)

print("\nRetrieved Context:")
print(context)

print("\nAnswer:")
print(result[0]["generated_text"])