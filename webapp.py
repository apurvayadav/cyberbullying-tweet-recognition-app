# importing libraries

from ctypes import alignment
from urllib import response
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import pandas as pd
import numpy as np
import re
import string
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from nltk.tokenize import RegexpTokenizer
from nltk import PorterStemmer, WordNetLemmatizer
from functions import *
import pickle

# Page title

image = Image.open('images/logo.png')

st.image(image, use_column_width= True)

st.write('''
# Cyberbulling Tweet Recognition App

This app predicts the nature of the tweet into 6 Categories.
* Age
* Ethnicity
* Gender
* Religion
* Other Cyberbullying
* Not Cyberbullying

***
''')

# Text Box
st.header('Enter Tweet ')
tweet_input = st.text_area("Tweet Input", height= 150)
print(tweet_input)
st.write('''
***
''')

# print input on webpage
st.header("Entered Tweet text ")
if tweet_input:
    tweet_input
else:
    st.write('''
    ***No Tweet Text Entered!***
    ''')
st.write('''
***
''')

# Output on the page
st.header("Prediction")
if tweet_input:
    prediction = custom_input_prediction(tweet_input)
    if prediction == "Age":
        st.image("images/age_cyberbullying.png",use_column_width= True)
    elif prediction == "Ethnicity":
        st.image("images/ethnicity_cyberbullying.png",use_column_width= True)
    elif prediction == "Gender":
        st.image("images/gender_cyberbullying.png",use_column_width= True)
    elif prediction == "Not Cyberbullying":
        st.image("images/not_cyberbullying.png",use_column_width= True)
    elif prediction == "Other Cyberbullying":
        st.image("images/other_cyberbullying.png",use_column_width= True)
    elif prediction == "Religion":
        st.image("images/religion_cyberbullying.png",use_column_width= True)
else:
    st.write('''
    ***No Tweet Text Entered!***
    ''')

st.write('''***''')

# About section
expand_bar = st.expander("About")
expand_bar.markdown('''
* **Source Code:** [https://github.com/apurvayadav/cyberbullying-tweet-recognition-app](https://github.com/apurvayadav/cyberbullying-tweet-recognition-app)
* **Dataset:** [https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification](https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification)
''')