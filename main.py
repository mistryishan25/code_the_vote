import streamlit as st
import random

# Set the page configuration
st.set_page_config(page_title="Login Page", layout="centered")

# Function to create a login card
def create_login_card(profile_name, profile_description):
    st.markdown(f"### {profile_name}")
    st.write(profile_description)
    if st.button(f"Login as {profile_name}"):
        st.session_state.logged_in = True
        st.session_state.profile = profile_name
        st.experimental_rerun()

# Main login page
def main_login_page():
    st.title("Login Page")

    col1, col2 = st.columns(2)

    with col1:
        create_login_card("Profile 1", "Login as a voter")

    with col2:
        create_login_card("Profile 2", "Login as a business")

# Function to generate random data for the leaderboard
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

# Leaderboard page
def leaderboard_page():
    st.title(f"Leaderboard - {st.session_state.profile}")

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

# Main logic
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    leaderboard_page()
else:
    main_login_page()
