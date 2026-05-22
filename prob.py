def message_passing():
    messages = []
    question_words = ("how", "when", "what", "where", "why")

    while True:
        user_input = input("Enter your message: ")

        if user_input.lower() == "\end":
            break

        capitalized = user_input.capitalize()

        if user_input.lower().startswith(question_words):
            messages.append(capitalized + "?")
        else:
            messages.append(capitalized + ".")

    return " ".join(messages)


print(message_passing()) 