# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 08:03:40 2020

@author: VIDYA
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("rr.pkl","rb")
rr=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(perimeter_worst,texture_worst,smoothness_worst,concave_points_worst,radius_se):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=rr.predict([[perimeter_worst,texture_worst,smoothness_worst,concave_points_worst,radius_se]])
    print(prediction)
    return prediction



def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    perimeter_worst = st.text_input("perimeter_worst","Type Here")
    texture_worst = st.text_input("texture_worst","Type Here")
    smoothness_worst = st.text_input("smoothness_worst","Type Here")
    concave_points_worst = st.text_input("concave points_worst","Type Here")
    radius_se = st.text_input("radius_se","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(perimeter_worst,texture_worst,smoothness_worst,concave_points_worst,radius_se)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    