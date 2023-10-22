import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_plotly_events import plotly_events
import requests
# add streamlit lottie
from streamlit_lottie import st_lottie
from streamlit_plotly_events import plotly_events

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_penguin = load_lottieurl(
    "https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json"
)
st_lottie(lottie_penguin, height=200)
st.title("Streamlit Plotly Events + Lottie Example: Penguins")


df = pd.read_csv(r"/workspaces/ughhhh/streamlit-app/component_examples/pages/penguins.csv")
fig = px.scatter(df, x="bill_length_mm", y="bill_depth_mm", color='species', color_discrete_map={'Adelie': 'blue', 'Chinstrap': 'green', 'Gentoo': 'red'})
selected_point = plotly_events(fig, click_event=True)
if len(selected_point) == 0:
 st.stop()
selected_x_value = selected_point[0]["x"]
selected_y_value = selected_point[0]["y"]
df_selected = df[
 (df["bill_length_mm"] == selected_x_value)
 & (df["bill_depth_mm"] == selected_y_value)
]
st.write("Data for selected point:")
st.write(df_selected)
