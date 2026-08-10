from transformers import pipeline

# Load translation model
translator = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
)

# English text
text = "Machine learning is changing the world."

# Translate English → French
result = translator(text)

print("English:")
print(text)

print("\nFrench:")
print(result[0]["translation_text"])