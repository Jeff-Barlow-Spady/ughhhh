import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
st.title("Palmer's Penguins")
# Bring in the CSV file
penguins_df = pd.read_csv(
    r'/workspaces/ughhhh/streamlit-app/penguin_app/penguins.csv')
st.write(penguins_df.head())

st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')
selected_species = st.selectbox('What species would you like to visualize?', [
                                'Adelie', 'Gentoo', 'Chinstrap'])
selected_x_var = st.selectbox('What do you want the x variable to be?', [
                              'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y?', [
                              'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
penguins_df = pd.read_csv(
    r'/workspaces/ughhhh/streamlit-app/penguin_app/penguins.csv')
penguins_df = penguins_df, title=f"Scatterplot of {selected_species} Penguins"]
alt_chart = (
    alt.Chart(penguins_df)
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,

    )
)
st.altair_chart(alt_chart)
