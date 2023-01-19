Import streamlit 
import json

# Open the JSON file
with open('data.json', 'r') as file:
    # Load the data from the file
    data = json.load(file)

# Extract the data you want to use
print(data['key'])
