import streamlit as st
import requests
import pandas as pd
#from streamlit_chat import message
from streamlit_chat import message




st.markdown("""# Harry Potter chat AI""")

#query = st.text_input('User:')

url ='https://verbamachina5-oi5egss6cq-ew.a.run.app/predict'

#?input1=hello&modeldir=harry'



input_history= []
output_history= []
#st.write(st.session_state['value'])




if "input_history" not in st.session_state:
    st.session_state["input_history"] = []

if "output_history" not in st.session_state:
    st.session_state["output_history"] = []

input_ = st.text_input("you:")
if input_:
    st.session_state["input_history"].append(input_)


parameters = dict(
           input1=input_,
           modeldir='harry')

response_api = requests.get(url, params=parameters).json()
harry=response_api['response']
st.session_state["output_history"].append(harry)

if st.session_state["input_history"]:
        for i in range(len(st.session_state["input_history"])):
            message(st.session_state["input_history"][i], key=str(i) + '_user', avatar_style="adventurer", is_user=True)
            message(st.session_state["output_history"][i+1], key=str(i) + '_bot', avatar_style="lorelei", seed=123, is_user=False)



#placeholder = st.empty()  # placeholder for latest message


#st.markdown(f'{input_history}')
#st.markdown(f'{st.session_state}')
#placeholder = st.empty()
