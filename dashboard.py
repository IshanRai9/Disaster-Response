import streamlit as st
from analyze_text import summaries

st.title("Real-Time Disaster Alerts")
st.write("Fetching latest disaster-related data...")

for summary in summaries:
    st.write("-", summary)