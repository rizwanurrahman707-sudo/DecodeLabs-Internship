print("=== Rule-Based AI Chatbot ===")
while True:
    user = input("you: ").lower()
    if user == "hello" or user =="hi":
        print("Bot:Hello! How can I help you?")
    elif user == "how are you":
        print("Bot:I am fine.Thanks for asking!")
    elif user =="what is your name":
        print("Bot:my name is rule-based AI Chatbot.")
    elif user =="who made you":
        print("Bot:I was created using python and if-else statements by Rizwan")
    elif user =="what do you know about decode":
        print("Bot: DecodeLabs is an organization that provides AI, programming, and technology training through practical projects and internships.")
    elif user == "good morning":
        print("Bot: Good Morning! Have a great day!")
    elif user == "good afternoon":
        print("Bot: Good Afternoon!")
    elif user == "good evening":
        print("Bot: Good Evening!")
    elif user == "good night":
        print("Bot: Good Night! Sweet dreams.")
    elif user == "thank you":
        print("Bot: You're welcome!")
    elif user =="bye" or user =="exit":
        print("Bot:Goodbye! Have a nice day!")
        break
    else:
        print("Bot:Sorry,I don'tunderstand.")
    