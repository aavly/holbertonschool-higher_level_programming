#!/usr/bin/python3
"""
4. Develop a Simple API using Python with Flask
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

users = {
    "bobby": {
        "username": "bobby",
        "name": "Bobby",
        "age": 12,
        "city": "Berlin"
        },
    "kazza": {
        "username": "kazza",
        "name": "Kazza",
        "age": 21,
        "city": "Moscow"
        }
}


@app.route("/")
def home():
    return "<p>Welcome to the Flask API!</p>"


@app.route("/data")
def serving_json_data():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user')
def add_user():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username required"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(debug=True)
