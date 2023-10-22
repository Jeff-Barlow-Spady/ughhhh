import streamlit as st
import pandas as pd

st.set_page_config(layout='wide', page_icon=":tree:")
st.title("Roots For Trees Inventory")
st.write(
    """
    An App to Examine and Visualize Inventory for Roots For Trees
    """
)

#@st.cache_data(persist=True)
trees_df = pd.read_csv(
    r"/workspaces/ughhhh/streamlit-app/pretty_trees/Root_for_Trees_Inventory_20231022.csv")
type = st.sidebar.multiselect(
    "Tree or Shrub",
    trees_df["tree_or_shrub"].unique())
if owners:
    trees_df = trees_df[
trees_df["tree_or_shrub"].isin(type)]
DF_GROUPED = pd.DataFrame(
    trees_df.groupby(["neighbourhood"]).count()["species"])

DF_GROUPED.columns = ["tree_count"]
##########################################################################

trees_df_map = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df_map = trees_df_map.sample(n=1000, replace=True)
st.map(trees_df_map)

tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Area Chart"])
with tab1:
   st.line_chart(DF_GROUPED)
with tab2:
    st.bar_chart(DF_GROUPED)
with tab3:
    st.area_chart(DF_GROUPED)