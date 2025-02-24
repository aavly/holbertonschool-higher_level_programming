#!/usr/bin/python3
"""
5. API Security and Authentication Techniques
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()
auth2 = HTTPTokenAuth(scheme='Bearer')
jwt = JWTManager(app)


# Create a list of users and their hashed pw's
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user


# Use a secret key for token generation and validation
app.config['JWT_SECRET_KEY'] = 'secret_key123'


# Protect Routes with Basic Authentication
    # Use the @auth.login_required decorator to protect certain routes
@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user()["username"])


# Using basic authentication
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted"), 200



# JWT-based Authentication
# Create a route /login where users can log in with their credentials
# ... and receive a JWT token
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(identity={"username": username, "role": user["role"]})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Bad username or password"}), 401


# JWT Protected Route - Accessible only with valid JWT token
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return jsonify(message="JWT Auth: Access Granted")

@app.route('/protected')
def protected():
    return jsonify(message="This is a protected route"), 200


# Implement Role-based Access Control:
@auth.get_user_roles
def get_user_roles(user):
    return user["role"]

# Admin-only route
@app.route('/admin')
@jwt_required()
def admin_route():
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        return jsonify(message="Hello, admin user!"), 200
    return jsonify(message="Access forbidden: Admins only!"), 403


# Role-based protected route
# Use the `get_jwt_identity` method to get user info from the token
# ...and check the user's role
@app.route('/admin_only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify(error="Admin access required"), 403
    return jsonify(message="Admin Access: Granted"), 200


# Custom Error Handlers 
    # Using Flask-JWT-Extended's decorators 

@auth.error_handler
def unauthorized():
    return jsonify({"error": "Unauthorized Access"}), 401

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run(debug=True)
