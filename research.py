import streamlit as st 

def show_guide():
    # Guide/Research
    st.title("How AI Reads Language")

    st.write("""
    Welcome!
    This interactive tool demonstrates how Artificial Intelligence uses one of the fundamental building blocks of Natural Language Processing (NLP): Tokenization to understand human language.

    But first, let's learn about what tokenization is and why it is important for AI to understand different languages.""")


    st.subheader("What is AI and what is the importance of Natural Language Processing (NLP)?")
    st.write("Just as natural language is how we humans comunicate with each other, Natural Language Processing (NLP) is how we teach computers to understand human language. NLP is a field of Artificial Intelligence that focuses on the interaction between computers and humans through natural language. It enables machines to read, understand, and derive meaning from human languages. NLP bridges the gap between human and machine.")

    st.subheader("What is Tokenization and why is it important for AI to understand human language?")
    st.write("Tokenization is the process of converting string characters (words, letters, or punctuation) into a series of integers, or tokens that can be used by machine learning algorithms. Tokenization is a crucial step in NLP because it allows AI models to process and analyze text data effectively. By breaking down text into smaller units, AI can better understand the structure and meaning of language, enabling tasks such as sentiment analysis, language translation, and information retrieval.")

    st.subheader("NLP handling for different languages")
    st.write("Now, handling text in different language may pose challenges for AI models especially for non-Latin scripts. A signifiant amount of data and text that AI has been trained on has been in English or similar languages and this can lead to difficulties in processing that have different grammatical structures, spacing rules, and characters.")

    st.subheader("Why Persian is challenging for AI to understand?")
