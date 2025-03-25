import ollama 

class Chatbot:
    def __init__(self):  # ✅ FIXED: Changed _init_ to __init__
        self.conversation_history = "You are an AI assistant that answers questions based on context.\n"

    def get_response(self, user_input):
        """Generate a response while maintaining context."""
        self.conversation_history += f"User: {user_input}\nAssistant:"

        response = ollama.chat(
            model="llama3.2:latest",
            messages=[{"role": "user", "content": self.conversation_history}]
        )

        bot_reply = response['message']['content']
        self.conversation_history += f"{bot_reply}\n"
        return bot_reply

def main():
    chatbot = Chatbot()
    print("Chatbot is ready! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
