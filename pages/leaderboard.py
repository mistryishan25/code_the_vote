import streamlit as st
import random

# Set the page configuration
st.set_page_config(page_title="Leaderboard", layout="wide")

# Create a title for the app
st.title("Leaderboard")

# Generate random data for the leaderboard
def generate_leaderboard_data(num_entries):
    leaderboard = []
    for i in range(num_entries):
        entry = {
            "name": f"Person {i+1}",
            "rank": random.randint(1, 100),
            "progress": random.randint(0, 50)
        }
        leaderboard.append(entry)
    return leaderboard

# Generate leaderboard data for 50 people
leaderboard_data = generate_leaderboard_data(50)

# Sort the leaderboard by rank in increasing order
leaderboard_data = sorted(leaderboard_data, key=lambda x: x["rank"])

# Function to create a card with a progress bar
def create_card(name, rank, progress):
    st.markdown(f"### {name} (Rank: {rank})")
    st.write(f"Rank: {rank}")
    st.write(f"Progress: {progress}/50")
    st.progress(progress / 50)

# Loop through the leaderboard data and create cards
for person in leaderboard_data:
    create_card(person["name"], person["rank"], person["progress"])
    st.markdown("---")  # Add a horizontal line for better separation
