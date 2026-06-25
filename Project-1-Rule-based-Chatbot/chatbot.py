print("Welcome to the Rule-Based AI Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower().strip()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
