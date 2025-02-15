import streamlit as st
import re
from collections import Counter

st.set_page_config(page_title="Login Page", page_icon="🔐")

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

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
    st.balloons()

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

        sentence_freq = Counter(sentences)
        repeated_sentences = {s: count for s, count in sentence_freq.items() if count > 1}

        return char_count, word_count, sentence_count, repeated_words, repeated_sentences

    st.title("📊 Text Analysis Tool")

    text_input = st.text_area("Enter your text here:")

    if st.button("🔍 Analyze"):
        if text_input.strip():
            char_count, word_count, sentence_count, repeated_words, repeated_sentences = analyze_text(text_input)
            st.subheader("📌 Analysis Results")
            st.write(f"*Total Characters:* {char_count}")
            st.write(f"*Total Words:* {word_count}")
            st.write(f"*Total Sentences:* {sentence_count}")

            st.subheader("🔄 Repeated Words")
            if repeated_words:
                st.json(repeated_words)  # ✅ Correct JSON format
            else:
                st.write("✅ No repeated words found.")  # ✅ Fixed

            st.subheader("🔁 Repeated Sentences")
            if repeated_sentences:
                st.json(repeated_sentences)  # ✅ Correct JSON format
            else:
                st.write("✅ No repeated sentences found.")  # ✅ Fixed
