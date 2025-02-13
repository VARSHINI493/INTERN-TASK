import streamlit as st
import sqlite3
import hashlib
import re
from collections import Counter

# Configure Streamlit page
st.set_page_config(page_title="Login & Registration", page_icon="🔐")

# Database setup
conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE, password TEXT)")
conn.commit()

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register a user
def register_user(username, password):
    hashed_password = hash_password(password)
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Username already exists

# Function to check login
def check_login(username, password):
    hashed_password = hash_password(password)
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    return c.fetchone() is not None

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "text_input" not in st.session_state:
    st.session_state.text_input = ""

# Sidebar for login and registration
st.sidebar.title("🔑 User Authentication")
auth_choice = st.sidebar.radio("Choose an option:", ["Login", "Register"])

# 🔹 **Registration Section**
if auth_choice == "Register":
    st.sidebar.subheader("📝 Create a New Account")
    new_username = st.sidebar.text_input("👤 Choose a Username", key="new_username")
    new_password = st.sidebar.text_input("🔑 Choose a Password", type="password", key="new_password")
    confirm_password = st.sidebar.text_input("🔑 Confirm Password", type="password", key="confirm_password")

    if st.sidebar.button("Register"):
        if new_password == confirm_password:
            if register_user(new_username, new_password):
                st.sidebar.success("✅ Registration Successful! Please log in.")
            else:
                st.sidebar.error("❌ Username already exists. Try a different one.")
        else:
            st.sidebar.error("❌ Passwords do not match!")

# 🔹 **Login Section**
elif auth_choice == "Login":
    st.sidebar.subheader("🔐 Login to Your Account")
    username = st.sidebar.text_input("👤 Username", key="login_username")
    password = st.sidebar.text_input("🔑 Password", type="password", key="login_password")

    if st.sidebar.button("Login"):
        if check_login(username, password):
            st.session_state.authenticated = True
            st.session_state.username = username  # Store username in session state
            st.sidebar.success("✅ Login Successful!")
            st.rerun()
        else:
            st.sidebar.error("❌ Invalid Username or Password")

# 🔹 **If Logged In, Show App**
if st.session_state.authenticated:
    st.success(f"🎉 Welcome, {st.session_state.username}!")
    st.snow()

    # TEXT ANALYSIS TOOL
    def analyze_text(text):
        char_count = len(text)
        words = [word.lower() for word in text.split()]
        word_count = len(words)
        sentences = re.split(r'[.!?]', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        sentence_count = len(sentences)

        word_freq = Counter(words)
        repeated_words = {word: count for word, count in word_freq.items() if count > 1}

        single_word_repeated = sum(1 for count in word_freq.values() if count == 2)
        double_word_repeated = sum(1 for count in word_freq.values() if count == 3)
        triple_word_repeated = sum(1 for count in word_freq.values() if count == 4)

        return char_count, word_count, sentence_count, single_word_repeated, double_word_repeated, triple_word_repeated

    st.title("📊 Text Analysis Tool")

    # Input section
    text_input = st.text_area("Enter your text here:", value=st.session_state.text_input)

    col1, col2 = st.columns([1, 1])

    # Clear button
    with col1:
        if st.button("Clear"):
            st.session_state.text_input = ""
            st.session_state.submitted = False
            st.rerun()

    # Submit button
    with col2:
        if st.button("Submit"):
            st.session_state.text_input = text_input
            st.session_state.submitted = True
            st.rerun()

    # Check if input text is provided and show analysis
    if st.session_state.submitted:
        if text_input.strip():
            char_count, word_count, sentence_count, single_word_repeated, double_word_repeated, triple_word_repeated = analyze_text(text_input)

            # Display Analysis Results
            st.subheader("📌 Analysis Results")
            st.write(f"📜 **Total Characters:** {char_count}")
            st.write(f"📖 **Total Words:** {word_count}")
            st.write(f"📝 **Total Sentences:** {sentence_count}")
            st.write(f"🔄 **Single Word Repeated Count:** {single_word_repeated}")
            st.write(f"🔁 **Double Word Repeated Count:** {double_word_repeated}")
            st.write(f"🔂 **Triple Word Repeated Count:** {triple_word_repeated}")

    # Logout Button
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.username = None
        st.rerun()
