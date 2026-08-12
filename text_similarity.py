from transformers import pipeline

# Load sentence similarity model
model = pipeline(
    "text-classification",
    model="cross-encoder/stsb-roberta-base"
)

sentence1 = "Machine learning is a part of artificial intelligence."
sentence2 = "Artificial intelligence includes machine learning."

result = model(
    f"{sentence1} [SEP] {sentence2}"
)

print("Sentence 1:", sentence1)
print("Sentence 2:", sentence2)
print("Result:", result)