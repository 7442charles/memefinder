import json
import os
import re
import time
from PIL import Image
import pytesseract

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Folder containing images
image_folder = '../memes/'

# Initialize a dictionary to store image data
image_data = {}

# Function to clean the extracted text, convert it to lowercase, and remove special characters and unnecessary spaces
def clean_text(text):
    # Remove special characters, extra spaces, and line breaks, and convert to lowercase
    cleaned_text = re.sub(r'[^\w\s]', '', text).strip().lower()

    # Remove text combinations representing new lines
    cleaned_text = cleaned_text.replace('\n', ' ').replace('\r', ' ')

    # Remove extra spaces again after replacing new lines
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    return cleaned_text

# Check if the JSON file already exists
if os.path.isfile('image_data.json'):
    # If it exists, read the existing JSON data
    with open('image_data.json', 'r') as json_file:
        existing_data = json.load(json_file)

        # Get the list of existing image names
        existing_image_names = list(existing_data.keys())
else:
    # If it doesn't exist, initialize the existing image names list as empty
    existing_image_names = []

# Start time tracking
start_time = time.time()

# Loop through all files in the image folder
print("Starting extraction...")
for filename in os.listdir(image_folder):
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
        # Check if the image name is already in the existing image names list
        if filename in existing_image_names:
            # print(f"Skipping {filename} as it already exists in the JSON file.")
            continue

        # Load and preprocess the image
        image_path = os.path.join(image_folder, filename)
        image = Image.open(image_path)

        # Perform OCR
        extracted_text = pytesseract.image_to_string(image)
        print(image_path)

        # Clean, lowercase, remove special characters, unnecessary spaces, and text combinations representing new lines
        cleaned_text = clean_text(extracted_text)

        # Create an entry for the image in the dictionary
        image_data[filename] = {
            "image_path": image_path,
            "image_text": cleaned_text  # Leave it as an empty string if no meaningful text
        }

# Calculate the elapsed time
elapsed_time = time.time() - start_time

# Update the existing JSON data with the new image data
existing_data.update(image_data)

# Save the updated image data to the JSON file
output_file = 'image_data.json'
with open(output_file, 'w') as json_file:
    json.dump(existing_data, json_file, indent=4, ensure_ascii=False)  # Ensure_ascii=False for non-ASCII characters

print(f"Text from {len(image_data)} images has been extracted, cleaned, and saved to {output_file}.")
print(f"Elapsed time: {elapsed_time:.2f} seconds")
