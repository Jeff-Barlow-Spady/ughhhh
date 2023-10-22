import streamlit as st
from transformers import pipeline

st.title("Hugging Face Demo: Sentiment Analysis")

text = st.text_input("Enter Text to Analyze")
@st.cache_resource()
def get_model():
    return pipeline("sentiment-analysis")
model = get_model()
if text:
    result = model(text)
    st.write("Sentiment", result[0]["label"])
    st.write("Confidence", result[0]["score"])