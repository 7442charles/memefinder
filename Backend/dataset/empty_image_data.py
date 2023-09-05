import json

# Load the data from image_data.json
with open('image_data.json', 'r') as json_file:
    image_data = json.load(json_file)

# Initialize a dictionary to store objects with empty "image_text"
empty_image_text_data = {}

# Iterate through the image_data and filter objects with empty "image_text"
for image_name, image_info in image_data.items():
    if not image_info["image_text"]:
        empty_image_text_data[image_name] = image_info

# Save the filtered data to empty_image_text.json
with open('empty_image_text.json', 'w') as output_file:
    json.dump(empty_image_text_data, output_file, indent=4)

print(f"Extracted and saved {len(empty_image_text_data)} objects with empty 'image_text' to empty_image_text.json.")
