import streamlit as st

import numpy as np
import pandas as pd

st.markdown("""# Pesona AI
## Ask me anything""")

image = '/marvinabn/VerbaMachina/images.jpg'
#st.image(image, caption='Harry Bot',use_column_width=True)
st.image(image, caption= 'Harry', width=650)

query = st.text_input('User:')
