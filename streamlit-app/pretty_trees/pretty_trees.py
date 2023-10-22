import streamlit as st
import pandas as pd
st.set_page_config(layout='wide', page_icon=":tree:")
st.title("Trees of San Fransisco")
st.write(
    """
    This app analyzes San Fransisco trees, data provided by SF DPW
    """
)

#@st.cache_data(persist=True)
trees_df = pd.read_csv(
    r"/workspaces/ughhhh/streamlit-app/trees_app/trees.csv")

DF_DBH_GROUPED = pd.DataFrame(
    trees_df.groupby(["dbh"]).count()["tree_id"]
).reset_index()

DF_DBH_GROUPED.columns = ["tree_count"]
##########################################################################


col1, col2, col3 = st.columns(3, gap='large')
with col1:
   st.line_chart(DF_DBH_GROUPED)
with col2:
    st.bar_chart(DF_DBH_GROUPED)
with col3:
    st.area_chart(DF_DBH_GROUPED)