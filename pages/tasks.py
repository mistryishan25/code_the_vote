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

    # st.header("Stats")
    accomplished_tasks = random.randint(0, 50)
    st.markdown(f"### Accomplished Tasks: {accomplished_tasks}")
    # st.progress(accomplished_tasks / 50)

    st.header("Tasks")

    # Generate task data for the gallery
    tasks = generate_task_data("Task", 8)

    # Create two columns for the gallery
    col1, col2 = st.columns(2)

    # Loop through the tasks and create tiles
    for i, task in enumerate(tasks):
        col = col1 if i % 2 == 0 else col2
        with col:
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
