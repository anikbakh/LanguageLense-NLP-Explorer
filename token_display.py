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
    html = """
    <div style="
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        align-items: center;
    ">
    """

    for i, token in enumerate(tokens):
        color = colors[i % len(colors)]
        html += f"""
        <span style="
            background-color: {color};
            color: black;
            padding: 6px 10px;
            border-radius: 8px;
            font-weight: bold;
            white-space: nowrap;
        ">
            {token}
        </span>
        """

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)