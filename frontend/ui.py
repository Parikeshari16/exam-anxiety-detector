# Placeholder for Streamlit frontend
import streamlit as st
from model.bert_model import predict_anxiety

st.title("AI Exam Anxiety Detector")

text = st.text_area("Enter your thoughts:")
if st.button("Check Anxiety"):
    result = predict_anxiety(text)
    st.write("Predicted Anxiety Level:", result)
