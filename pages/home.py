import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to PalFiction! 👋")

st.sidebar.success("Select a character above.")

st.markdown(
    """
    PalFiction - choose a character:
"""
)

st.image('./characters_overview.png', caption='Choose your chracter')
#st.image('../images.jpg', caption='Spongebob')
#st.image('../images.jpg', caption='')
#st.image('../images.jpg', caption='')
