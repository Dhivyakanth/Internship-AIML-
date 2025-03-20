# Chatbot that loads data from a document and answers questions

def load_knowledge(file_path):
    """Loads knowledge from a document and returns a dictionary."""
    knowledge = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if "|" in line:
                question, answer = line.strip().split(" | ", 1)
                knowledge[question] = answer
    return knowledge

def get_answer(question, knowledge):
    """Returns an answer based on the question or a default response."""
    return knowledge.get(question, "I'm not sure about that. Please ask something else.")

# Main chatbot loop
if __name__ == "__main__":
    knowledge_file =  r"E:/ML modal/Chatbot_basics/knowledge.txt" # Path to the knowledge document
    knowledge_base = load_knowledge(knowledge_file)

    print("Chatbot: Hello! Ask me a question. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = get_answer(user_input, knowledge_base)
        print(f"Chatbot: {response}")
