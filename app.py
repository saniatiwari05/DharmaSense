from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load JSON dataset
with open("festival_data.json", "r", encoding="utf-8") as f:
    festival_data = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/festivals")
def get_festivals():
    return jsonify(festival_data)

@app.route("/api/festival/<name>")
def get_festival_by_name(name):
    for festival in festival_data["festival_intelligence_engine"]:
        if festival["festival_or_tithi"].lower() == name.lower():
            return jsonify(festival)
    return jsonify({"error": "Festival not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
