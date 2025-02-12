import streamlit as st
import pandas as pd

# Set background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e0f2e9;
    }
    h1, h2 {
        color: #1b5e20; /* Dark Green */
    }
    .stNumberInput label, .stTextInput label, .stSelectbox label {
        color: #1b5e20; /* Dark Green */
    }
    .stButton>button {
        background-color: #1b5e20; /* Dark Green */
        color: white;
    }
       
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("Battery Heroes & GIGAGREEN - Kick-Off Meeting Poll")
st.write("st.write("Help us find the best time and focus for our upcoming meeting! We are initially planning for a 90-minute session, so please consider this when selecting your preferred time slots.")
")

# Step 1: Preferred Month
st.header("1️⃣ When would you prefer the meeting to take place?")
months = st.multiselect(
    "Select all months that work for you:",
    ["April", "May", "June"]
)

# Step 2: Preferred Days of the Week
st.header("2️⃣ Which days of the week work best for you?")
days = st.multiselect(
    "Select your preferred days:",
    ["Monday-Wednesday", "Thursday-Friday"]
)

# Step 3: Preferred Time Slot
st.header("3️⃣ What time slots are best for you?")
time_slots = st.multiselect(
    "Select all time slots that work:",
    ["08:00-10:00", "12:00-14:00", "16:00-18:00"]
)

# Step 4: Meeting Goals
st.header("4️⃣ What is the main goal of this meeting for you?")
goals = st.multiselect(
    "Choose the most relevant:",
    [
        "Networking & making new contacts",
        "Agreeing on a collaboration framework",
        "Discussing challenges & potential synergies",
        "Other (please specify)"
    ]
)
other_goal = ""
if "Other (please specify)" in goals:
    other_goal = st.text_input("Please specify your goal:")

# Step 5: Name, Project, and Email
st.header("5️⃣ Your Contact Info (Optional)")
name = st.text_input("Your Name")
project = st.selectbox(
    "Which project do you represent?",
    ["BatWoMan", "Giga Green", "greenSPEED", "NoVOC", "GigaBat", "Batmachine"]
)
email = st.text_input("Your Email")

# Save responses
if st.button("Submit Your Response"):
    responses = {
        "Name": name,
        "Project": project,
        "Email": email,
        "Preferred Months": months,
        "Preferred Days": days,
        "Preferred Time Slots": time_slots,
        "Meeting Goals": goals,
        "Other Goal": other_goal
    }
    df = pd.DataFrame([responses])
    df.to_csv("meeting_poll_responses.csv", mode='a', header=False, index=False)
    st.success("Thank you! Your response has been recorded.")
