import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
from bokeh.plotting import figure
import altair as alt

st.title("The Trees of San Fransisco")

st.write(
    """This app analyzes trees in San Fransisco,\
          data kindly provided by SF DPW"""
)
@st.cache_data()
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
trees_df_sub = trees_df.dropna(subset=["longitude", "latitude"])
trees_df_sub = trees_df_sub.sample(n=1000)
st.map(trees_df_sub)
st.divider()
########################################################################################
st.subheader("Plotly")


fig = px.histogram(trees_df["dbh"])
st.plotly_chart(fig)

st.divider()
################################################################################################
trees_df['age'] = (pd.to_datetime('today') - pd.to_datetime(trees_df['date'])).dt.days
st.subheader("Seaborn")
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df['age'])
plt.xlabel('Age(Days)')
st.pyplot(fig_sb)

st.subheader('Matplotlib')
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df['age'])
plt.xlabel("Age (Days)")
st.pyplot(fig_mpl)
st.divider()

st.subheader('Bokeh')
scatterplot = figure(title = 'Bokeh Scatterplot')
scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
scatterplot.yaxis.axis_label = "site_order"
scatterplot.xaxis.axis_label = "dbh"
st.bokeh_chart(scatterplot)
st.divider()
#########################################################################
st.subheader("Altair")
#df_ctkr = trees_df.groupby(["caretaker"]).count()["tree_id"].reset_index()
#df_ctkr.column = ['caretaker', 'tree_count']
fig = alt.Chart(trees_df).mark_bar().encode(x= 'caretaker', y = 'count(*):Q')
st.altair_chart(fig)