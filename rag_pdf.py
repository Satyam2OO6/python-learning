from pypdf import PdfReader
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline

# -----------------------------
# 1. Read PDF
# -----------------------------
pdf_path = "document.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"

# -----------------------------
# 2. Split Text into Chunks
# -----------------------------
chunk_size = 500

chunks = [
    text[i:i + chunk_size]
    for i in range(0, len(text), chunk_size)
]

# -----------------------------
# 3. Load Embedding Model
# -----------------------------
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

document_embeddings = embedding_model.encode(
    chunks,
    convert_to_tensor=True
)

# -----------------------------
# 4. Ask a Question
# -----------------------------
question = input("Ask a question about the PDF: ")

question_embedding = embedding_model.encode(
    question,
    convert_to_tensor=True
)

# -----------------------------
# 5. Find Relevant Chunks
# -----------------------------
scores = util.cos_sim(
    question_embedding,
    document_embeddings
)[0]

best_indices = scores.topk(
    k=min(3, len(chunks))
).indices

context = "\n".join(
    chunks[i] for i in best_indices
)

# -----------------------------
# 6. Generate Answer
# -----------------------------
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

prompt = f"""
Answer the question using only the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

result = generator(
    prompt,
    max_new_tokens=100
)

print("\nAnswer:")
print(result[0]["generated_text"])