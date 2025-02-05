from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/disaster_alerts", methods=["GET"])
def get_alerts():
    alerts = summaries  # Processed disaster-related summaries
    return jsonify(alerts)

if __name__ == "__main__":
    app.run(debug=True)