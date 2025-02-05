from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/disaster_alerts", methods=["GET"])
def get_alerts():
    alerts = summaries  # Processed disaster-related summaries
    return jsonify(alerts)

if __name__ == "__main__":
    app.run(debug=True)

import streamlit as st

st.title("Real-Time Disaster Alerts")
st.write("Fetching latest disaster-related data...")

for summary in summaries:
    st.write("-", summary)
