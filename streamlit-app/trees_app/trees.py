import datetime as dt
import streamlit as st
import pandas as pd
import numpy as np
#import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

from bokeh.plotting import figure
import altair as alt

st.title("The Trees of San Fransisco")

st.write(
    """This app analyzes trees in San Fransisco,\
          data kindly provided by SF DPW"""
)
#@st.cache_data(persist=True)
trees_df = pd.read_csv(
    r"/workspaces/ughhhh/streamlit-app/trees_app/trees.csv")

DF_DBH_GROUPED = pd.DataFrame(
    trees_df.groupby(["dbh"]).count()["tree_id"]
).reset_index()

DF_DBH_GROUPED.columns = ["dbh", "tree_count"]
###########################################################################
st.divider()
st.subheader("Built-in Plotting")
st.divider()
st.line_chart(DF_DBH_GROUPED, x="dbh", y="tree_count")
st.divider()

DF_DBH_GROUPED_NEW = DF_DBH_GROUPED.assign(new_col=np.random.randn(len(DF_DBH_GROUPED)) * 500)
st.line_chart(DF_DBH_GROUPED_NEW, x="dbh", y=["tree_count", "new_col"])
#####################################################################################
st.divider()
st.subheader("Mapping")

st.divider()
trees_df_sub = trees_df.dropna(subset=["longitude", "latitude"])
trees_df_sub = trees_df_sub.sample(n=1000)


st.map(trees_df_sub)
st.divider()
########################################################################################
#st.subheader("Plotly")

#fig = px.histogram(trees_df["dbh"])
#st.plotly_chart(fig)

##st.divider()
################################################################################################
trees_df["date"] = pd.to_datetime(trees_df["date"])  # convert to datetime object
trees_df["age"] = (pd.Timestamp.now()) - (trees_df["date"]).dt.days
st.subheader("Seaborn")
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df["age"])
plt.xlabel("Age(Days)")
st.pyplot(fig_sb)




st.subheader("Matplotlib")
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df["age"])
plt.xlabel("Age (Days)")
st.pyplot(fig_mpl)
st.divider()

st.subheader("Bokeh")
scatterplot = figure(title="Bokeh Scatterplot")
scatterplot.scatter(trees_df["dbh"], trees_df["site_order"])
scatterplot.yaxis.axis_label = "site_order"
scatterplot.xaxis.axis_label = "dbh"
st.bokeh_chart(scatterplot)
st.divider()
#########################################################################
st.subheader("Altair")
# df_ctkr = trees_df.groupby(["caretaker"]).count()["tree_id"].reset_index()
# df_ctkr.column = ['caretaker', 'tree_count']
fig = alt.Chart(trees_df).mark_bar().encode(x="caretaker", y="count(*):Q")
st.altair_chart(fig)
