from click import echo
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import requests
def load_lottieurl(url: str):
 r = requests.get(url)
 if r.status_code != 200:
        return None
    return r.json()
lottie_airplane = load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_jhu1lqdz.json')
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
airport_distance_df = pd.read_csv(r"/workspaces/ughhhh/streamlit-app/job_app_example/airport_location.csv")
with st.echo():
    #load necessary data
    airport_distance_df = pd.read_csv(r"/workspaces/ughhhh/streamlit-app/job_app_example/airport_location.csv")

"""
From some quick googling, I found that the Haversine distance is
a good approximation for distance. At least good enough to get the
distance between airports! Haversine distances can be off by up to .5%
because the Earth is not actually a sphere. It looks like the latitudes
and longitudes are in degrees, so I'll make sure to have a way to account
for that as well. The Haversine distance formula is labeled below,
followed by an implementation in Python
"""
st.image('/workspaces/ughhhh/streamlit-app/job_app_example/haversine.png')
with st.echo():
from math import atan2, cos, radians, sin, sqrt
def haversine_distance(long1, lat1,
 long2, lat2, degrees=False):
    # degrees vs radians
    if degrees == True:
        long1 = radians(long1)
        lat1 = radians(lat1)
        long2 = radians(long2)
        lat2 = radians(lat2)
    # haversine formula
    a = (
        sin((lat2 - lat1) / 2) ** 2
        + cos(lat1) * cos(lat2) * sin((long2 - long1) / 2) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c #The radius of earth in KM
    return distance
from math import atan2, cos, radians, sin, sqrt
def haversine_distance(long1, lat1,
    long2, lat2, degrees=False):
    # degrees vs radians
    if degrees == True:
        long1 = radians(long1)
        lat1 = radians(lat1)
        long2 = radians(long2)
        lat2 = radians(lat2)
    # haversine formula
    a = (
        sin((lat2 - lat1) / 2) ** 2
        + cos(lat1) * cos(lat2) * sin((long2 - long1) / 2) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c #The radius of earth in KM
    return distance
"""
Now, we need to test out our function! The
distance between the default points is
18,986 kilometers, but feel free to try out
your own points of interest.
"""
long1 = st.number_input('Longitude 1', value = 2.55)
long2 = st.number_input('Longitude 2', value = 172.00)
lat1 = st.number_input('Latitude 1', value = 49.01)
lat2 = st.number_input('Latitude 2', value = -43.48)
test_distance = haversine_distance(long1 = long1, long2 = long2,
        lat1 = lat1, lat2 = lat2, degrees=True)
st.write('Your distance is: {} kilometers'.format(int(test_distance)))
"""
We have the Haversine distance implemented, and we also have
proven to ourselves that it works reasonably well.
Our next step is to implement this in a function!
"""
def get_distance_list(airport_dataframe,
                        airport_code):
    df = airport_dataframe.copy()
    