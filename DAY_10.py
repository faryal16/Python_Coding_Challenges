import random  

# Predefined responses  
responses = {  
    "hello": ["Hi there! How can I help you?", "Hello! What's up?", "Hey! Nice to see you! 😊"],  
    "what's your name": ["I'm a simple chatbot created by you! 🤖", "Call me ChatBot3000!", "Just a friendly bot here to chat!"],  
    "tell me a joke": [  
        "Why don’t scientists trust atoms? Because they make up everything! 😂",  
        "Why did the math book look sad? Because it had too many problems! 📖😆",  
        "Why was the computer cold? It left its Windows open! 🥶💻"  
    ],  
    "goodbye": ["Bye! Have a great day! 😊", "Goodbye! Hope to chat again soon!", "See ya later, alligator! 🐊"],  
}

# Store user-trained responses in a dictionary
custom_responses = {}

def chatbot_response(user_input):  
    """Returns a chatbot response from predefined or user-trained responses."""  
    user_input = user_input.lower().strip()  

    # ✅ Check user-trained responses  
    if user_input in custom_responses:  
        return random.choice(custom_responses[user_input])  

    # ✅ Check predefined responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])  

    return "I don’t understand. You can teach me by saying: 'Train: [your input] = [my response]'"

def train_bot(command):  
    """Trains the chatbot by saving custom responses in memory."""  
    try:  
        if command.lower().startswith("train:"):  
            command = command.replace("train:", "", 1).strip()
            if "=" not in command:
                return "⚠️ Please use the format: Train: [your input] = [my response]"

            user_input, bot_reply = command.split("=", 1)  # ✅ Split only at first '='
            user_input = user_input.strip().lower()  
            bot_reply = bot_reply.strip()  

            # ✅ Store and retrieve responses correctly
            if user_input in custom_responses:  
                custom_responses[user_input].append(bot_reply)  
            else:  
                custom_responses[user_input] = [bot_reply]  

            return f"Got it! I've learned a new response for '{user_input}'. 🧠✨"
    except Exception as e:  
        return f"Oops! Use the format: Train: [your input] = [my response]. Error: {e}"

# ✅ Chat loop that remembers trained responses  
print("\n\t\t🤖 ChatBot: Hello! Type 'exit' to end the chat.\n")  
while True:  
    user_input = input("You: ").strip()  

    if user_input.lower() == "exit":  
        print("\n🤖 ChatBot: Goodbye! Have a great day! 😊")
        break  
    elif user_input.lower().startswith("train:"):  
        print(f"🤖 ChatBot: {train_bot(user_input)}\n")  
    else:  
        print(f"🤖 ChatBot: {chatbot_response(user_input)}\n")
