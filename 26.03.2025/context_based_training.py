import nltk
import ollama

# ✅ Download necessary NLTK resources
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

def extract_keywords(text):
    """Extracts meaningful keywords including actions (verbs), objects, and places."""
    words = nltk.word_tokenize(text)  # Tokenize input
    tagged_words = nltk.pos_tag(words)  # POS tagging
    
    # Extract nouns, proper nouns, and verbs (actions)
    keywords = [word for word, tag in tagged_words if tag in ("NN", "NNS", "NNP", "NNPS", "VB", "VBP", "VBZ")]
    
    return keywords

def generate_keyword_summary(keywords, user_input):
    """Generates a response based on extracted keywords and user intent."""
    keyword_phrase = " ".join(keywords)

    # ✅ Improve prompt to ensure AI understands context
    prompt = (f"Analyze the following question and answer it based on extracted keywords.\n\n"
              f"Question: {user_input}\n"
              f"Extracted Keywords: {keyword_phrase}\n\n"
              f"Provide a **brief but informative response** that directly addresses the user's intent.")

    response = ollama.chat(
        model="llama3.2:latest",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"].strip()

def get_llama_answer(user_input):
    """Processes user input and generates a structured response."""
    keywords = extract_keywords(user_input)

    if not keywords:
        return "I couldn't determine relevant keywords."

    keyword_display = f"Keywords: {', '.join(keywords)}"
    summary_response = generate_keyword_summary(keywords, user_input)

    return f"{keyword_display}\n\n{summary_response}"

# ✅ Chatbot Loop
while True:
    user_input = input("Ask me something (or type 'exit' to quit): ").strip()
    
    if user_input.lower() == "exit":
        break
    
    answer = get_llama_answer(user_input)
    print(answer)
