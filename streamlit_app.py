import streamlit as st
import re
from collections import Counter

# Function to analyze text
def analyze_text(text):
    char_count = len(text)

    words = re.findall(r'\b\w+\b', text.lower())  # Extract words properly
    word_count = len(words)

    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(sentences)

    # Count repeated single words
    word_freq = Counter(words)
    repeated_single_words = {word: count for word, count in word_freq.items() if count > 1}

    # Count repeated double-word phrases
    double_word_phrases = [" ".join(words[i:i+2]) for i in range(len(words)-1)]
    double_word_freq = Counter(double_word_phrases)
    repeated_double_words = {phrase: count for phrase, count in double_word_freq.items() if count > 1}

    # Count repeated triple-word phrases
    triple_word_phrases = [" ".join(words[i:i+3]) for i in range(len(words)-2)]
    triple_word_freq = Counter(triple_word_phrases)
    repeated_triple_words = {phrase: count for phrase, count in triple_word_freq.items() if count > 1}

    return char_count, word_count, sentence_count, repeated_single_words, repeated_double_words, repeated_triple_words

# Streamlit UI
st.title("📊 Text Analysis Tool")

# Session state for text input
if "text" not in st.session_state:
    st.session_state.text = ""

# Function to clear text area
def clear_text():
    st.session_state.text = ""

# Input Section
text_input = st.text_area("Paste or type your text here:", value=st.session_state.text, key="text", height=200)

# Buttons
col1, col2 = st.columns(2)
with col1:
    submit_btn = st.button("✅ Submit")
with col2:
    clear_btn = st.button("❌ Clear", on_click=clear_text)

# Analysis Results
if submit_btn and text_input.strip():
    char_count, word_count, sentence_count, single_words, double_words, triple_words = analyze_text(text_input)

    st.subheader("📌 Analysis Results")
    st.write(f"**Total Characters:** {char_count}")
    st.write(f"**Total Words:** {word_count}")
    st.write(f"**Total Sentences:** {sentence_count}")

    st.subheader("🔄 Repeated Single Words")
    if single_words:
        st.json(single_words)
    else:
        st.success("No repeated words found.")

    st.subheader("🔁 Repeated Double Word Phrases")
    if double_words:
        st.json(double_words)
    else:
        st.success("No repeated double word phrases found.")

    st.subheader("🔂 Repeated Triple Word Phrases")
    if triple_words:
        st.json(triple_words)
    else:
        st.success("No repeated triple word phrases found.")
