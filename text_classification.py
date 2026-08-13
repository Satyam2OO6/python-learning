from transformers import pipeline

# Load a pre-trained text classification model
classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

texts = [
    "I love learning artificial intelligence.",
    "This is a terrible experience."
]

# Predict classes
results = classifier(texts)

for text, result in zip(texts, results):
    print("Text:", text)
    print("Label:", result["label"])
    print("Confidence:", round(result["score"], 3))
    print()