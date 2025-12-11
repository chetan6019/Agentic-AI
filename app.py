import streamlit as st
import json
import requests

API_URL = "http://localhost:8000/email/"

st.title("📧Customer Email Generator")

question = st.text_area("Enter your query here...", height=300)

if st.button("Submit"):
    if not question.strip():
        st.warning("Please enter your query related to refund request, delivery issues and misc.")
    else:
        with st.spinner("Replying..."):
            payload = {
                "input": question,
                "thread_id": "001"
            }
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                st.success(response.json()["final_response"])
            else:
                st.error(f"Failed: {response.json()}")
