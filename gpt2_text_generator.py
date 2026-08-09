from transformers import pipeline

# Load GPT-2
generator = pipeline(
    "text-generation",
    model="gpt2"
)

# Starting prompt
prompt = "Artificial intelligence will"

# Generate text
result = generator(
    prompt,
    max_new_tokens=80,
    num_return_sequences=1,
    do_sample=True,
    temperature=0.7
)

print("Generated Text:")
print(result[0]["generated_text"])