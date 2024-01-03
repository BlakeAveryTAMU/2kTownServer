from flask import Flask, request, jsonify
from src import controller

app = Flask(__name__)

@app.route("/api/")
def home():
    return "Home"

@app.route("/api/add_user", methods=["POST"])
def add_user_endpoint():

    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    team_id = data.get("team_id")

    if not all([email, password, team_id]):
        return jsonify({"error": "Missing data"}), 400

    controller.add_user(email, password, team_id)
    return jsonify({"message": "User added successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True)