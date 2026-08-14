from transformers import pipeline

# Load zero-shot classification model
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

text = "I am learning Python and building machine learning projects."

# Possible categories
labels = [
    "Programming",
    "Machine Learning",
    "Sports",
    "Cooking"
]

# Classify text
result = classifier(
    text,
    candidate_labels=labels
)

print("Text:", text)
print("\nClassification:")

for label, score in zip(
    result["labels"],
    result["scores"]
):
    print(label, ":", round(score, 3))