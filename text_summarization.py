from transformers import pipeline

# Load summarization model
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

# Long text
text = """
Machine learning is a branch of artificial intelligence that allows
computers to learn patterns from data and make predictions without
being explicitly programmed for every task. Deep learning is a part
of machine learning that uses neural networks with multiple layers.
It is widely used in computer vision, natural language processing,
speech recognition, recommendation systems, and many other areas.
"""

# Generate summary
result = summarizer(
    text,
    max_length=60,
    min_length=20,
    do_sample=False
)

print("Summary:")
print(result[0]["summary_text"])