import streamlit as st
from google.cloud import storage
import torch

# Connect to GCP bucket
storage_client = storage.Client.from_service_account_json('./samplename-378401-845b4a7b63f0.json')
bucket = storage_client.get_bucket('verbamachina')

# Load NLP chatbot model
model_blob = bucket.blob('models/pytorch_model.bin')
#if (last_modified = model_blob)
model_blob.download_to_filename('model.bin')
model = torch.load('model.bin')

# Define user interface
st.title('NLP Chatbot')
user_input = st.text_input('You: ')
if st.button('Submit'):
    response = model.predict(user_input)
    st.text('Bot: ' + response)
