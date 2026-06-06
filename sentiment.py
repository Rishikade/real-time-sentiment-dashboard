import streamlit as st
from transformers import pipeline

# Load model only once
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

classifier = load_model()

def analyze_sentiment(text):
    try:
        result = classifier(text)[0]

        return {
            "label": result["label"],
            "score": result["score"]
        }

    except Exception as e:
        return {
            "label": "ERROR",
            "score": 0,
            "message": str(e)
        }