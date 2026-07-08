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
    st.write("""
    Persian is considered a low-resource language in the field of NLP, meaning that there is less available data and research compared to high-resource languages like English. This in addition to the unique characteristics of Persian, it can be challenging for AI models to process and understand Persian Text. For example, Persian is written in a script that is different from the Latin alphabet, and it has its own set of grammatical rules and structures. Additionally, Persian has a rich morphology, meaning that words can have many different forms depending on their context. This can make it difficult for AI models to accurately tokenize and analyze Persian text.")
    
    Other challenges include:
    
    - Persian is written from right to left
    - Persian uses both full spaces and half spaces between words, which can affect tokenization and word segmentation.
    - Many Persian letters have different forms depending on their position in a word; if it is the first letter, middle, or last letter
    - A word in Persian can have different forms depending on its position in a sentence, which can make it difficult for AI models to accurately identify and analyze words.
    """)
    
    st.subheader("What comes after tokenization?")
    st.write("So what is the purpose of tokens and tokenization? After a sentence is segmented into words or letters (or what the specific tokenizer is designed to do), the next step is to convert these tokens into numerical representations that can be processed by machine learning algorithms.")
