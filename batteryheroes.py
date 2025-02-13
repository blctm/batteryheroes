import streamlit as st
import pandas as pd
import smtplib
from email.message import EmailMessage

# Title
st.title("Battery Heroes & GIGAGREEN - Kick-Off Meeting Poll")
st.write("Help us find the best time and focus for our upcoming meeting! We are initially planning for a 90-minute session, so please consider this when selecting your preferred time slots.")


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

# Function to send email
def send_email(csv_filename):
    sender_email = "your_email@gmail.com"  # Your email
    receiver_email = "your_email@gmail.com"  # Where responses go
    password = "your_app_password"  # Use an **App Password**, not your real password!

    msg = EmailMessage()
    msg["Subject"] = "New Battery Heroes Meeting Response"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(f"A new response has been submitted. See the attached CSV.")

    # Attach CSV
    with open(csv_filename, "rb") as f:
        msg.add_attachment(f.read(), maintype="text", subtype="csv", filename=csv_filename)

    # Send email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.send_message(msg)
        st.success("✅ Response submitted & emailed successfully!")
    except Exception as e:
        st.error(f"❌ Failed to send email: {e}")

# Save responses & send email
if st.button("Submit Your Response"):
    responses = {
        "Name": name, "Project": project, "Email": email,
        "Preferred Months": ", ".join(months), "Preferred Days": ", ".join(days),
        "Preferred Time Slots": ", ".join(time_slots), "Meeting Goals": ", ".join(goals),
        "Other Goal": other_goal
    }
    df = pd.DataFrame([responses])

    # Save CSV
    csv_filename = "meeting_poll_responses.csv"
    df.to_csv(csv_filename, mode='a', header=False, index=False)

    # Send email with CSV
    send_email(csv_filename)
