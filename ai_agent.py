from transformers import pipeline

# Load language model
generator = pipeline(
    "text-generation",
    model="gpt2"
)

# Simple tools
def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Invalid calculation"


def search_knowledge(question):
    knowledge = {
        "python": "Python is a programming language.",
        "machine learning": "Machine learning allows computers to learn from data.",
        "deep learning": "Deep learning uses neural networks."
    }

    for key, value in knowledge.items():
        if key in question.lower():
            return value

    return "No information found."


# AI Agent
def agent(question):

    question_lower = question.lower()

    # Decide which tool to use
    if any(char.isdigit() for char in question_lower):
        try:
            result = calculator(question_lower)
            return "Calculator result: " + str(result)
        except:
            pass

    result = search_knowledge(question)

    if result != "No information found.":
        return result

    # Use GPT-2 if no tool matches
    response = generator(
        question,
        max_new_tokens=50,
        num_return_sequences=1
    )

    return response[0]["generated_text"]


# Chat with agent
while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Agent: Goodbye!")
        break

    answer = agent(question)

    print("Agent:", answer)