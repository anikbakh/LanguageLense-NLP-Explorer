import streamlit as st
from nlp_tokenizers import whitespace_tokenizer, english_tokenizer, persian_tokenizer
from token_display import display_tokens

# CSS
st.markdown("""
<style>

/* App background */
.stApp {
    background-color: #F8F7F2;
}

/* Main text */
h1, h2, h3, h4, h5, h6,
p, label, li, ul, ol {
    color: #222222 !important;
}

/* Buttons */
.stButton > button {
    background-color: black !important;
    color: white !important;
    border: 1px solid black !important;
}

.stButton > button:hover {
    background-color: #333333 !important;
    color: white !important;
}

.stButton > button * {
    color: white !important;
}

/* Selectbox label */
.stSelectbox label {
    color: #222222 !important;
}

/* Closed selectbox */
.stSelectbox [data-baseweb="select"] {
    background-color: black !important;
    border-radius: 6px;
}

.stSelectbox [data-baseweb="select"] * {
    color: white !important;
}

/* Open dropdown menu */
[data-baseweb="popover"] {
    background-color: black !important;
}

/* Dropdown list */
ul[role="listbox"] {
    background-color: black !important;
}

/* Dropdown options */
li[role="option"] {
    background-color: black !important;
    color: white !important;
}

li[role="option"] * {
    color: white !important;
}

/* Hovered option */
li[role="option"]:hover {
    background-color: #333333 !important;
}

/* Selected option */
li[aria-selected="true"] {
    background-color: #444444 !important;
    color: white !important;
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
    "I am going to the bookstore tomorrow. | من فردا به کتاب‌فروشی می‌روم": {
        "English": "I am going to the bookstore tomorrow.",
        "Persian": "من فردا به کتاب‌فروشی می‌روم.",
        "Explanation": """
        **Why this matters: Persian uses special spacing rules**

        Persian uses invisible spaces called half-spaces in words like 
        "کتاب‌فروشی" and "می‌روم".

        These spaces help Persian readers understand words, but they can be 
        challenging for AI because they are different from normal spaces used 
        in English.
        """,
        "English Tokenizer": "English word splitter (NLTK)",
        "Persian Tokenizer": "Persian language word splitter (Hazm)"
    },

    "Tokenization is fundamental to Natural Language Processing | توکن‌سازی برای پردازش زبان طبیعی بنیادین است": {
        "English": "Tokenization is fundamental to Natural Language Processing.",
        "Persian": "توکن‌سازی برای پردازش زبان طبیعی بنیادین است.",
        "Explanation": """
        **Why this matters: Persian words can be built from multiple parts**

        Persian often combines meaningful parts together to create words.

        For example, "توکن‌سازی" combines two parts using a half-space. 
        AI needs to recognize these patterns to correctly understand Persian text.
        """,
        "English Tokenizer": "English word splitter (NLTK)",
        "Persian Tokenizer": "Persian language word splitter (Hazm)"
    },

    "Artificial intelligence is changing the way we communicate | هوش مصنوعی شیوهٔ ارتباط مردم را تغییر می‌دهد": {
        "English": "Artificial intelligence is changing the way we communicate.",
        "Persian": "هوش مصنوعی شیوهٔ ارتباط مردم را تغییر می‌دهد.",
        "Explanation": """
        **Why this matters: Languages organize information differently**

        English and Persian do not build sentences in the same way.

        Persian verbs can include extra information inside the word. For example,
        "می‌دهد" includes a verb prefix that English expresses differently.
        AI needs language-specific tools to understand these differences.
        """,
        "English Tokenizer": "English word splitter (NLTK)",
        "Persian Tokenizer": "Persian language word splitter (Hazm)"
    }
}


selected = st.selectbox(
    "Select a sentence:",
    list(examples.keys())
)


selected_data = examples[selected]


english_text = selected_data["English"]
persian_text = selected_data["Persian"]


# Tokenize
english_tokens = english_tokenizer(english_text)
persian_tokens = persian_tokenizer(persian_text)


# Display tokenization first
col1, col2 = st.columns(2)


with col1:
    st.subheader("English Tokenization")

    st.write("Original Sentence:")
    st.write(english_text)

    st.write("How AI breaks it into parts:")
    display_tokens(english_tokens)

    st.write(f"Total Tokens: {len(english_tokens)}")


with col2:
    st.subheader("Persian Tokenization")

    st.write("Original Sentence:")
    st.write(persian_text)

    st.write("How AI breaks it into parts:")
    display_tokens(persian_tokens)

    st.write(f"Total Tokens: {len(persian_tokens)}")


# Explanation after visualization
st.subheader("Why is this example important?")
st.markdown(selected_data["Explanation"])


# Tokenizer information
st.subheader("Tools Used")

col1, col2 = st.columns(2)

with col1:
    st.write("**English:**")
    st.write(selected_data["English Tokenizer"])

with col2:
    st.write("**Persian:**")
    st.write(selected_data["Persian Tokenizer"])

#----------------------------