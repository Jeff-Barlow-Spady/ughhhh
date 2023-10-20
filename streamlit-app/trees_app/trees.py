import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt

st.title("The Trees of San Fransisco")

st.write(
    """This app analyzes trees in San Fransisco,\
          data kindly provided by SF DPW"""
)
trees_df = pd.read_csv(r"/workspaces/ughhhh/streamlit-app/trees_app/trees.csv")

df_dbh_grouped = pd.DataFrame(
    trees_df.groupby(["dbh"]).count()["tree_id"]
).reset_index()

df_dbh_grouped.columns = ["dbh", "tree_count"]
###########################################################################
st.divider()
st.subheader("Built-in Plotting")
st.divider()
st.line_chart(df_dbh_grouped, x="dbh", y="tree_count")
st.divider()

df_dbh_grouped["new_col"] = np.random.randn(len(df_dbh_grouped)) * 500
st.line_chart(df_dbh_grouped)
#####################################################################################
st.divider()
st.subheader("Mapping")

st.divider()
trees_df = trees_df.dropna(subset=["longitude", "latitude"])
trees_df = trees_df.sample(n=1000)
st.map(trees_df)
st.divider()
########################################################################################
st.subheader("Plotly")


fig = px.histogram(trees_df["dbh"])
st.plotly_chart(fig)

st.divider()
st.subheader("Seaborn")
trees_df['age'] = (pd.to_datetime('today') - pd.to_datetime(trees_df['date'])).dt.days