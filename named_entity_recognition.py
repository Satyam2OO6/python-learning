from transformers import pipeline

# Load NER model
ner = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple"
)

# Input text
text = """
Elon Musk founded SpaceX and Tesla.
SpaceX is headquartered in the United States.
"""

# Find entities
results = ner(text)

# Display results
for entity in results:
    print("Entity:", entity["word"])
    print("Type:", entity["entity_group"])
    print("Confidence:", round(entity["score"], 3))
    print()