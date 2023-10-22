import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import requests
def load_lottieurl(url: str):
 r = requests.get(url)
 if r.status_code != 200:
        return None
    return r.json()
lottie_airplane = load_lottieurl('https://assets4.lottiefiles.com/
packages/lf20_jhu1lqdz.json')
st_lottie(lottie_airplane, speed=1, height=200, key="initial")
st.title('Example Job Application Question')
st.write('by Jeff Barlow-Spady - inspired by Tyler Richards')
st.subheader('Question 1: Airport Distance')
"""
The first exercise asks us 'Given the table of airports and
locations (in latitude and longitude) below,
write a function that takes an airport code as input and
returns the airports listed from nearest to furthest from
the input airport.' There are three steps here:
1. Load the data
2. Implement a distance algorithm
3. Apply the distance formula across all airports other than the input
4. Return a sorted list of the airports' distances
"""
airport_distance_df = pd.read_csv()