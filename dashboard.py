import streamlit as st

st.title("Real-Time Disaster Alerts")
st.write("Fetching latest disaster-related data...")

for summary in summaries:
    st.write("-", summary)