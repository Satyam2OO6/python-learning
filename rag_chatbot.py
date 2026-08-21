import chromadb
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# -----------------------------
# 1. Create Knowledge Base
# -----------------------------
documents = [
    "Python is a programming language.",
    "Machine learning allows computers to learn from data.",
    "Deep learning uses neural networks with multiple layers.",
    "CNNs are commonly used for image classification.",
    "RNNs are designed for sequential data.",
    "Transformers use attention mechanisms.",
    "RAG combines information retrieval with text generation."
]

# -----------------------------
# 2. Create ChromaDB
# -----------------------------
client = chromadb.Client()

collection = client.create_collection(
    name="knowledge_base"
)

# -----------------------------
# 3. Create Embeddings
# -----------------------------
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

embeddings = embedding_model.encode(
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
# 5. Load Text Generation Model
# -----------------------------
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

# -----------------------------
# 6. Chat Loop
# -----------------------------
while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    # Create query embedding
    query_embedding = embedding_model.encode(
        [question]
    ).tolist()

    # Retrieve relevant documents
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    context = "\n".join(
        results["documents"][0]
    )

    # Create prompt
    prompt = f"""
Answer the question using only the context.

Context:
{context}

Question:
{question}

Answer:
"""

    # Generate answer
    response = generator(
        prompt,
        max_new_tokens=100
    )

    print("\nChatbot:", response[0]["generated_text"])