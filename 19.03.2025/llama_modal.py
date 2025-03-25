import os
import string
import nltk
import ollama
from nltk.corpus import reuters

# ✅ Step 1: Download Reuters dataset
nltk.download('reuters')
nltk.download('punkt')

# ✅ Step 2: Create 'data' directory
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

# ✅ Step 3: Save Reuters articles as text files
for fileid in reuters.fileids():
    article_text = ' '.join(reuters.words(fileid))
    filename = os.path.join(data_dir, fileid.replace("/", "_") + ".txt")
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(article_text)

print(f"✅ Reuters articles saved in '{data_dir}/' for processing.")

# ✅ Step 4: Read and preprocess text data
punctuation = string.punctuation.replace('.', '')  # Keep full stops
text_data = ""

def is_hidden(filepath):
    return os.path.basename(filepath).startswith('.')

# Read all text files from 'data' folder
for filename in os.listdir(data_dir):
    filepath = os.path.join(data_dir, filename)
    if not is_hidden(filepath):
        with open(filepath, encoding="utf-8") as infile:
            for line in infile:
                if line.strip():  # Ignore empty lines
                    # Remove all punctuation except full stops
                    for char in punctuation:
                        line = line.replace(char, '')
                    text_data += line + " "

print(f"✅ Loaded {len(text_data)} characters of text.")

# ✅ Step 5: Function to Generate Text using Llama 3.2 (Limited Words)
def generate_sentence(prompt, num_words=100):
    """Generates text using the locally installed Llama 3.2 model and limits the output to a specific word count."""
    
    # Format the prompt
    full_prompt = f"Continue the following text naturally but generate only {num_words} words:\n{prompt}"

    # Query Llama 3.2 via Ollama
    response = ollama.chat(
        model="llama3.2:latest",  # ✅ Ensure correct model name
        messages=[{"role": "user", "content": full_prompt}]
    )

    # Extract the generated text
    generated_text = response['message']['content']

    # Limit output to 'num_words' by splitting and joining words
    word_list = generated_text.split()
    limited_text = " ".join(word_list[:num_words])  # Take only the first 'num_words' words

    # Print the trimmed text
    print("\n🔹 Generated Text (Limited to", num_words, "words):\n")
    print(limited_text)

# ✅ Step 6: Get User Input and Generate Text
while True:
    user_input = input("\nEnter a starting sentence (or type 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        print("👋 Exiting...")
        break
    
    # Ask user for word limit
    try:
        num_words = int(input("Enter the number of words to generate: "))
    except ValueError:
        print("⚠️ Invalid input! Using default limit of 100 words.")
        num_words = 100

    generate_sentence(user_input, num_words)
