import json

# Load data from "image_text_data.json"
with open('../image_data.json', 'r') as json_file:
    image_data = json.load(json_file)

# Initialize a dictionary to store categorized data
categories = {
    "single": [],
    "coworker": [],
    "friends": [],
    "zodiac signs": [],
    "alcohol": [],
    "boys": [],
    "broke": [],
    "gaming": [],
    "programming": [],
    "boobs": [],
    "kenyan": []
}

# Define keywords or phrases associated with each category
category_keywords = {
    "single": ["single", "relationship", "dating"],
    "coworker": ["coworker", "office", "work"],
    "friends": ["friend", "friendship"],
    "zodiac signs": ["zodiac", "horoscope", "astrology"],
    "alcohol": ["alcohol", "drink", "bar"],
    "boys": ["boys", "men", "guys"],
    "broke": ["broke", "poor", "money"],
    "gaming": ["gaming", "game", "console"],
    "programming": ["programming", "code", "developer"],
    "boobs": ["boobs", "breasts"],
    "kenyan": ["kenyan", "Kenya"]
}

# Categorize the data based on keywords
for filename, image_info in image_data.items():
    image_text = image_info["image_text"].lower()  # Convert text to lowercase for case-insensitive matching
    for category, keywords in category_keywords.items():
        for keyword in keywords:
            if keyword in image_text:
                categories[category].append({
                    "filename": filename,
                    "image_path": image_info["image_path"],
                    "image_text": image_info["image_text"]
                })
                break  # Break if a match is found in this category

# Save categorized data to one JSON file with arrays for each category
output_file = 'categorized_data.json'
with open(output_file, 'w') as json_file:
    json.dump(categories, json_file, indent=4)

print("Data has been categorized and saved to categorized_data.json.")
