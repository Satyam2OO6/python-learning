from transformers import pipeline

# Load a BERT-based sentiment model
model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Input text
texts = [
    "I love machine learning.",
    "This project is very difficult."
]

# Predict sentiment
results = model(texts)

# Display results
for text, result in zip(texts, results):
    print("Text:", text)
    print("Sentiment:", result["label"])
    print("Confidence:", result["score"])
    print()