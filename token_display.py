import streamlit as st

colors = [
    "#D6EAF8",
    "#D5F5E3",
    "#FCF3CF",
    "#FADBD8",
    "#E8DAEF",
    "#FDEBD0",
    "#D4EFDF",
    "#EBF5FB"
]

def display_tokens(tokens):
    sentence = ""

    for i, token in enumerate(tokens):
        sentence += (
            f'<span style="'
            f'background-color:{colors[i % len(colors)]};'
            f'padding:4px 8px;'
            f'border-radius:6px;'
            f'color:black;'
            f'font-weight:bold;'
            f'margin-right:4px;'
            f'">{token}</span> '
        )

    st.markdown(sentence, unsafe_allow_html=True)