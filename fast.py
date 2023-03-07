from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import pandas as pd
#import tokenizer
#import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
#http://127.0.0.1:8000/predict?input=hello

app.state.model1 = AutoModelForCausalLM.from_pretrained('./models/harry')
app.state.model2 = AutoModelForCausalLM.from_pretrained('./models/spongebob')

app.state.tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-small')

# http://127.0.0.1:8000/predict?pickup_datetime=2012-10-06 12:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2
@app.get("/predict")
def predict(input1:str, modeldir:str):      # 1
    """
    we use type hinting to indicate the data types expected
    for the parameters of the function
    FastAPI uses this information in order to hand errors
    to the developpers providing incompatible parameters
    FastAPI also provides variables of the expected data type to use
    without type hinting we need to manually convert
    the parameters of the functions which are all received as strings
    """
    #from registry import load_model
    #from preprocessor import preprocess_features

    # X_pred = pd.DataFrame(dict(
    #        pickup_datetime=[pd.Timestamp(pickup_longitude, tz='UTC')],
    #        pickup_longitude=float(pickup_latitude),
    #        pickup_latitude=float(dropoff_longitude),
    #        dropoff_longitude=float(dropoff_longitude),
    #        dropoff_latitude=float(dropoff_latitude),
    #        passenger_count=float(passenger_count),
    # ))

    # model = load_model()
    
    if modeldir == "harry":
        model = app.state.model1
    else:
        model = app.state.model2
    # # X_processed = preprocess_features(X_pred)
    # pred = model.predict(input)

    # print("\n✅ prediction done: ", pred, "\n")
    # return {'Answer': pred}
    step = 0
    #How to get a tokenizer?
    
    #TODO Tokenizer and model outside the function
    tokenizer = app.state.tokenizer
    new_user_input_ids = tokenizer.encode(input1 + tokenizer.eos_token, return_tensors='pt') 
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids 
    chat_history_ids = model.generate( 
        bot_input_ids, max_length=200, 
        pad_token_id=tokenizer.eos_token_id,  
        no_repeat_ngram_size=3, 
        do_sample=True, 
        top_k=100, 
        top_p=0.3, 
        temperature = 0.3 
    ) 
    
    # pretty print last ouput tokens from bot
    response = ("Harry: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
    #print(model)
    return {"response": response}


@app.get("/")
def root():
    return {'greeting': 'Hello, VerbaMachina!'}
