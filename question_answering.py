from transformers import pipeline

# Load a BERT-based question answering model
qa = pipeline(
    "question-answering",
    model="deepset/bert-base-cased-squad2"
)

# Context
context = """
Machine learning is a branch of artificial intelligence.
It allows computers to learn patterns from data and make predictions.
Deep learning is a part of machine learning that uses neural networks
with multiple layers.
"""

# Question
question = "What is machine learning?"

# Get answer
result = qa(
    question=question,
    context=context
)

print("Question:", question)
print("Answer:", result["answer"])
print("Confidence:", round(result["score"], 3))