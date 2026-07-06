import streamlit as st
from nlp_tokenizers import whitespace_tokenizer, english_tokenizer, persian_tokenizer
from token_display import display_tokens

#CSS
st.markdown("""
<style>
.stApp {
    background-color: #00008A;
}

</style>
""", unsafe_allow_html=True)


#----------------------------
#Guide goes here
from research import show_guide
show_guide()  # Call the function to display the guide at the top of the app
#----------------------------


#----------------------------
#Enter your own text tool

st.title("Explore Your Own Text!")

text = st.text_area( "Enter a sentence and see how tokenization breaks it down:",
                    placeholder = "Example: I love learning about AI.")

tokenizer_choice = st.selectbox(
    "Choose a tokenization method:",
    (
        "Simple (Split on Spaces)",
        "Smart English Tokenizer",
        "Persian Tokenizer"
    )
)

# Analyze Button
if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter a sentence to analyze.")
    else:

        if tokenizer_choice == "Simple (Split on Spaces)":
            tokens = whitespace_tokenizer(text)
            explanation = """
                This tokenizer simply splits text wherever it finds a space.
                It is easy to understand, but it does not recognize punctuation
                or more complex language patterns.
                """

        elif tokenizer_choice == "Smart English Tokenizer":
            tokens = english_tokenizer(text)
            explanation = """
                This tokenizer is more advanced. It recognizes punctuation and follows
                English language rules to split text more accurately.
                """
        else:
            tokens = persian_tokenizer(text)
            explanation = """
                This tokenizer is designed for Persian text. Persian has unique spacing,
                character, and writing rules that require specialized NLP tools.
                """

        #Tokenized output
        st.subheader("Tokenized Output")
        display_tokens(tokens)
        
        #Original sentence and statistics
        st.subheader("Original Sentence")
        st.subheader(text)
        st.subheader("Statistics")
        st.write(f"Characters: {len(text)}")
        st.write(f"Tokens: {len(tokens)}")

        st.subheader("What Happened?")

        st.info(explanation)
#----------------------------


#----------------------------
#Compare Persian and English Tokenization
st.title("Chose one of the following sentences to see how tokenization works for English and Persian:")
examples = {
    "Sentence 1": {
        "English": "I love learning about AI.",
        "Persian": "من عاشق یادگیری در مورد هوش مصنوعی هستم."
        },

    "Sentence 2": {
        "English": "Tokenization is fundamental to Natural Language Processing.",
        "Persian": "توکن‌سازی برای پردازش زبان طبیعی بنیادین است."
        }
}

selected = st.selectbox("Select a sentence:", list(examples.keys()))

english_text = examples[selected]["English"]
persian_text = examples[selected]["Persian"]

english_tokens = english_tokenizer(english_text)
persian_tokens = persian_tokenizer(persian_text)


col1, col2 = st.columns(2)

with col1:
    st.subheader("English Tokenization")
    st.write(f"Original: {english_text}")
    st.write(f"Tokens: {english_tokens}")

    display_tokens(english_tokens)
    st.write(f"Total Tokens: {len(english_tokens)}")

with col2:
    st.subheader("Persian Tokenization")
    st.write(f"Original: {persian_text}")
    st.write(f"Tokens: {persian_tokens}")
    
    display_tokens(persian_tokens)  
    st.write(f"Total Tokens: {len(persian_tokens)}")