import streamlit as st
import re
from collections import Counter

st.set_page_config(page_title="Login Page", page_icon="🔐")

# Initialize session state for authentication and other variables
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "submitted" not in st.session_state:  # Initialize submitted in session state
    st.session_state.submitted = False
if "text_input" not in st.session_state:  # Initialize text_input in session state
    st.session_state.text_input = ""

st.title("🔐 Login Page")

# Hardcoded credentials (For demonstration purposes)
VALID_USERNAME = "admin"
VALID_PASSWORD = "123"

if not st.session_state.authenticated:
    username = st.text_input("👤 Username", key="username")
    password = st.text_input("🔑 Password", type="password", key="password")
    
    if st.button("Login"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.authenticated = True
            st.rerun()  # ✅ Fixed: Use st.rerun() instead of st.experimental_rerun()
        else:
            st.error("❌ Invalid Username or Password")
else:
    st.success("✅ Login Successful!")
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

        # Count single, double, and triple repeated words
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
