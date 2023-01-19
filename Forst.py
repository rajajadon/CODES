import streamlit as st
import json
st.file_uploader('upload the file',type=['pdf']
st.button('submit')
# Open the JSON file
with open('data.json', 'r') as file:
    # Load the data from the file
    data = json.load(file)

# Extract the data you want to use
print(data['key'])
