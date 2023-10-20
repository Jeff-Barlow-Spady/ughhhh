import streamlit as st
import pandas as pd

st.title("The Trees of San Fransisco")

st.write(
    """This app analyzes trees in San Fransisco,\
          data kindly provided by SF DPW"""
          
)
trees_df = pd.read_csv(r"/workspaces/ughhhh/streamlit-app/trees_app/trees.csv")
st.write(trees_df.head())