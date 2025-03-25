import json
import nltk
import re
from fuzzywuzzy import process  # Fuzzy string matching

# ✅ Download necessary NLTK resources
nltk.download("punkt")

def load_knowledge(file_path):
    """Loads knowledge from a document and returns a dictionary."""
    knowledge = {}
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if "|" in line:
                    question, answer = line.strip().split(" | ", 1)
                    formatted_question = normalize_text(question)
                    knowledge[formatted_question] = answer  # Store normalized keys
    except FileNotFoundError:
        print("Warning: Knowledge file not found.")
    return knowledge

def normalize_text(text):
    """Normalizes text by removing extra spaces and making it lowercase."""
    text = re.sub(r"\s+", "", text)  # Remove all spaces
    return text.lower()  # Convert to lowercase

def get_best_match(question, knowledge):
    """Finds the best matching question from the knowledge base."""
    formatted_question = normalize_text(question)
    
    # Use fuzzy matching to find the closest question
    best_match, score = process.extractOne(formatted_question, knowledge.keys())

    if score >= 80:  # Adjust the threshold as needed
        return knowledge[best_match]
    else:
        return "I'm not sure about that. Please ask something else."

if __name__ == "__main__":
    knowledge_file = r"E:/ML modal/Chatbot_basics/knowledge.txt"  # Path to the knowledge document
    knowledge_base = load_knowledge(knowledge_file)
    
    print("Chatbot: Hello! Ask me a question. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = get_best_match(user_input, knowledge_base)
        print(f"Chatbot: {response}")
