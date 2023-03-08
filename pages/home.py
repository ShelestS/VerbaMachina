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

st.image('/Users/marvinnaessig/code/ShelestS/VerbaMachina/images.jpg', caption='Harry Potter')
st.image('/Users/marvinnaessig/code/ShelestS/VerbaMachina/images.jpg', caption='Spongebob')
st.image('/Users/marvinnaessig/code/ShelestS/VerbaMachina/images.jpg', caption='')
st.image('/Users/marvinnaessig/code/ShelestS/VerbaMachina/images.jpg', caption='')
