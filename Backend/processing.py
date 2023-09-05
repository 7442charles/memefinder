import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to clean and preprocess text (replace with your clean_text function)
def clean_text(text):
    # Implement your text preprocessing here
    return text

# ANSI escape codes for text color
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Load the dataset from the specified folder
dataset_path = './dataset/image_data.json'

with open(dataset_path, 'r') as json_file:
    dataset = json.load(json_file)

# Extract image URLs and text from the dataset
image_urls = []
text_data = []
for image_id, image_info in dataset.items():
    if image_info['image_text']:
        image_urls.append(image_info['image_path'])
        text_data.append(clean_text(image_info['image_text']))

# Create TF-IDF vectors for the dataset text descriptions
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(text_data)

while True:
    # User's input text
    user_input = input("Enter text (or type 'exit' to quit): ")
    
    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        break

    # Preprocess user input (lowercase and clean)
    user_input = clean_text(user_input)

    # Calculate cosine similarities between user input and dataset descriptions
    user_tfidf = tfidf_vectorizer.transform([user_input])
    similarities = cosine_similarity(user_tfidf, tfidf_matrix)

    # Create a list to store matching image URLs
    matching_image_urls = []

    # Iterate through all similarities and corresponding image URLs
    for index, similarity_score in enumerate(similarities[0]):
        similarity_percentage = similarity_score * 100  # Convert similarity to percentage

        # Check if similarity is greater than zero
        if similarity_percentage > 0:
            matching_image_urls.append((similarity_percentage, image_urls[index]))

    # Sort matching URLs by similarity percentage in descending order
    matching_image_urls.sort(reverse=True)

    # Check if any matching image URLs were found
    if len(matching_image_urls) == 0:
        print(f"{RED}No meme matching your description found.{RESET}")
    else:
        # Print all image URLs that have a similarity greater than zero
        for similarity_percentage, image_url in matching_image_urls:
            print(f"{GREEN}Similarity percentage = {similarity_percentage:.2f}% | Image URL: {image_url}{RESET}")
