import streamlit as st
import pandas as pd

st.set_page_config(layout='wide', page_icon="🌳")
st.title("Trees of San Fransisco")
st.write(
    """
    This app analyzes San Fransisco trees, data provided by SF DPW
    """
)

#@st.cache_data(persist=True)
trees_df = pd.read_csv(
    r"streamlit-app/pretty_trees/trees.csv")
owners = st.sidebar.multiselect(
    "Tree Owner Filter",
    trees_df["caretaker"].unique())
if owners:
    trees_df = trees_df[
trees_df["caretaker"].isin(owners)]
DF_DBH_GROUPED = pd.DataFrame(
    trees_df.groupby(["dbh"]).count()["tree_id"])

DF_DBH_GROUPED.columns = ["tree_count"]
##########################################################################

trees_df_map = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df_map = trees_df_map.sample(n=1000, replace=True)
st.map(trees_df_map)

tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Area Chart"])
with tab1:
   st.line_chart(DF_DBH_GROUPED)
with tab2:
    st.bar_chart(DF_DBH_GROUPED)
with tab3:
    st.area_chart(DF_DBH_GROUPED)
