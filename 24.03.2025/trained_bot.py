import nltk
import ollama

# ✅ Download necessary NLTK resources
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

def extract_keywords(text):
    """Extracts relevant keywords from user input."""
    words = nltk.word_tokenize(text)  # Tokenize input
    tagged_words = nltk.pos_tag(words)  # POS tagging
    keywords = [word for word, tag in tagged_words if tag in ("NN", "NNS", "NNP", "NNPS")]  # Extract nouns
    return keywords

def generate_keyword_summary(keywords):
    """Generates a single paragraph summary for the keyword."""
    keyword_phrase = " ".join(keywords)

    # ✅ Prompt to generate a *concise* single-paragraph answer
    prompt = (f"Provide a single, well-structured paragraph that answers who, what, when, where, "
              f"why, and how about {keyword_phrase}. Keep the response informative but brief.")

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

    summary_response = generate_keyword_summary(keywords)

    return f"{keyword_display}\n\n{summary_response}"

# ✅ Chatbot Loop
while True:
    user_input = input("Ask me something (or type 'exit' to quit): ").strip()
    
    if user_input.lower() == "exit":
        break
    
    answer = get_llama_answer(user_input)
    print(answer)