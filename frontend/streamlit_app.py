# frontend/streamlit_app.py

import streamlit as st
import requests

st.set_page_config(page_title="SmartAdvisor Chatbot", layout="wide")

st.title("🤖 SmartAdvisor Chatbot")
st.write("Ask me anything about your orders, account, returns, and more.")

user_input = st.text_input("Enter your question:", "")

if st.button("Send") and user_input:
    response = requests.post("http://localhost:8000/chat", json={"question": user_input})
    if response.status_code == 200:
        data = response.json()
        st.markdown(f"**Classification (Decision Tree):** {data['classification']['decision_tree']}")
        st.markdown(f"**Classification (KNN):** {data['classification']['knn']}")
        st.markdown("---")
        st.markdown(f"**SmartAdvisor Response:**\n\n{data['ai_response']}")
    else:
        st.error("Something went wrong. Please try again.")
