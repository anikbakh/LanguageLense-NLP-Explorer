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
    html = ""

    for i, token in enumerate(tokens):
        color = colors[i % len(colors)]
        html += f"""
        <span style="
            background-color:{color};
            color:black;
            padding:6px 10px;
            border-radius:8px;
            margin-right:4px;
            display:inline-block;
            font-weight:bold;
            margin-bottom:6px;
        ">
            {token}
        </span>
        """

    st.markdown(html, unsafe_allow_html=True)