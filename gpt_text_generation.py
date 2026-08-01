# GPT-style Text Generation using Hugging Face Transformers

# Install first:
# pip install transformers torch

from transformers import pipeline

# Load a small GPT-2 model
generator = pipeline(
    "text-generation",
    model="gpt2"
)

# Starting text
prompt = "Machine learning is"

# Generate text
result = generator(
    prompt,
    max_new_tokens=50,
    num_return_sequences=1,
    temperature=0.8,
    do_sample=True
)

print(result[0]["generated_text"])