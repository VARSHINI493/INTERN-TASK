import streamlit as st
import re
from collections import Counter

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

if "text" not in st.session_state:
    st.session_state.text = ""

def clear_text():
    st.session_state.text = ""

text_input = st.text_area("Enter your text here:", value=st.session_state.text, key="text")

col1, col2 = st.columns(2)
with col1:
    analyze_btn = st.button("🔍 Analyze")
with col2:
    clear_btn = st.button("❌ Clear", on_click=clear_text)

if analyze_btn and text_input.strip():
    char_count, word_count, sentence_count, repeated_words, repeated_sentences = analyze_text(text_input)
    
    st.subheader("📌 Analysis Results")
    st.write(f"*Total Characters:* {char_count}")
    st.write(f"*Total Words:* {word_count}")
    st.write(f"*Total Sentences:* {sentence_count}")
    
    st.subheader("🔄 Repeated Words")
    if repeated_words:
        st.json(repeated_words)
    else:
        st.success("No repeated words found.")
    
    st.subheader("🔁 Repeated Sentences")
    if repeated_sentences:
        st.json(repeated_sentences)
    else:
        st.success("No repeated sentences found.")
