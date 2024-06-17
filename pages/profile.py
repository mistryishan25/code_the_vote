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
        create_login_card("Profile 1", "Description for Profile 1")

    with col2:
        create_login_card("Profile 2", "Description for Profile 2")

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

# Function to generate random task data
def generate_task_data(task_type, num_tasks):
    tasks = []
    for i in range(num_tasks):
        task = {
            "title": f"{task_type} Task {i+1}",
            "description": f"Description for {task_type.lower()} task {i+1}",
            "progress": random.randint(0, 100)
        }
        tasks.append(task)
    return tasks

# Profile page
def profile_page():
    st.title(f"Profile - {st.session_state.profile}")

    st.header("Stats")
    accomplished_tasks = random.randint(0, 50)
    st.markdown(f"### Accomplished Tasks: {accomplished_tasks}")
    st.progress(accomplished_tasks / 50)

    st.header("Tasks")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Individual Tasks")
        individual_tasks = generate_task_data("Individual", 5)
        for task in individual_tasks:
            with st.expander(task["title"]):
                st.write(task["description"])
                st.progress(task["progress"] / 100)

    with col2:
        st.subheader("Friend Tasks")
        friend_tasks = generate_task_data("Friend", 5)
        for task in friend_tasks:
            with st.expander(task["title"]):
                st.write(task["description"])
                st.progress(task["progress"] / 100)

    with col3:
        st.subheader("Group Tasks")
        group_tasks = generate_task_data("Group", 5)
        for task in group_tasks:
            with st.expander(task["title"]):
                st.write(task["description"])
                st.progress(task["progress"] / 100)

# Main logic
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    profile_page()
else:
    main_login_page()
