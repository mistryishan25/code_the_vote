import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Rewards", layout="wide")

# Create a title for the app
st.title("Reward Gallery")

# Function to create a card
def create_card(title, description, details, image_url=None):
    if image_url:
        st.image(image_url, width=375)
    with st.expander(title):
        st.markdown(f"### {description}")
        st.write(details)

# Reward data
rewards = [
    {
        "title": "Reward 1",
        "description": "This is reward 1",
        "details": "Details about reward 1...",
        "image_url": "https://via.placeholder.com/150"
    },
    {
        "title": "Reward 2",
        "description": "This is reward 2",
        "details": "Details about reward 2...",
        "image_url": "https://via.placeholder.com/150"
    },
    {
        "title": "Reward 3",
        "description": "This is reward 3",
        "details": "Details about reward 3...",
        "image_url": "https://via.placeholder.com/150"
    },
    {
        "title": "Reward 4",
        "description": "This is reward 4",
        "details": "Details about reward 4...",
        "image_url": "https://via.placeholder.com/150"
    },
    {
        "title": "Reward 5",
        "description": "This is reward 5",
        "details": "Details about reward 5...",
        "image_url": "https://via.placeholder.com/150"
    },
]

# Number of columns in the gallery
num_columns = 3

# Create columns for the gallery layout
columns = st.columns(num_columns)

# Loop through the rewards and create cards
for index, reward in enumerate(rewards):
    col = columns[index % num_columns]
    with col:
        create_card(reward["title"], reward["description"], reward["details"], reward["image_url"])
