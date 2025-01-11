from flask import Blueprint, request, jsonify, session

user_bp = Blueprint('user_bp', __name__)

USER_CREDENTIALS = {'username': 'admin', 'password': 'password123'}

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
        session['logged_in'] = True
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Invalid credentials!"}), 401

@user_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    return jsonify({"message": "Logged out successfully!"}), 200
