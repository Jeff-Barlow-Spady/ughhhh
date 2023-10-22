import streamlit as st
import pandas as pd
import pydeck as pdk


st.title("The Trees of San Fransisco")

st.write(
    """This app analyzes trees in San Fransisco,\
          data kindly provided by SF DPW"""
)
#@st.cache_data()
trees_df = pd.read_csv(r"/workspaces/ughhhh/streamlit-app/trees_app/trees.csv")
trees_df.dropna(how='any', inplace=True)

sf_init_view = pdk.ViewState(
    latitude=37.76,
    longitude=-122.4,
    zoom=11,
    pitch=40,
    )
hx_layer = pdk.Layer(
    "HexagonLayer",
    data=trees_df,
    get_position=["longitude", "latitude"],
    radius=100,
    elevation_scale=4,
    elevation_range=[0, 1000],
    pickable=True,
    extruded=True)
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=sf_init_view,
    layers=[hx_layer],
    tooltip={"text": "Number of trees: {elevationValue}"}
))
