import json

# Knowledge base stored as a dictionary
knowledge = {
    "What is AI?": "AI, or Artificial Intelligence, is the simulation of human intelligence in machines.",
    "What is Machine Learning?": "Machine Learning is a subset of AI that enables machines to learn from data.",
    "Who invented AI?": "The concept of AI was first introduced by Alan Turing and later developed by John McCarthy.",
    "What is Python?": "Python is a popular programming language used for AI, web development, and automation."
}

# Function to get an answer from the knowledge base
def get_answer(question):
    # Normalize input and match case-insensitively
    for key in knowledge.keys():
        if key.lower() == question.lower():
            return knowledge[key]
    return "I'm not sure about that. Please ask something else."

if __name__ == "__main__":
    print("Chatbot: Hello! Ask me a question. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = get_answer(user_input)
        print(f"Chatbot: {response}")
