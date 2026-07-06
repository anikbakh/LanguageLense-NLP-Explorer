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
    cols = st.columns(len(tokens))

    for i, token in enumerate(tokens):
        with cols[i]:
            st.markdown(
                f"""
                <div style="
                    background-color:{colors[i % len(colors)]};
                    color:black;
                    padding:12px;
                    border-radius:10px;
                    border:1px solid gray;
                    text-align:center;
                    font-weight:bold;
                    font-size:20px;
                ">
                {token}
                </div>
                """,
                unsafe_allow_html=True
            )