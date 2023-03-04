import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon= "🧑‍💻"
)

with open("WEB_README.md", "r") as f:
    st.markdown("".join(f.readlines()))
