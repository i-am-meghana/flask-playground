from flask import Blueprint, jsonify

jsonify_bp = Blueprint('jsonify_bp', __name__)

@jsonify_bp.route('/hello')
def hello():
    return jsonify({"message": "Hello, World!"})

@jsonify_bp.route('/echo', methods=['POST'])
def echo_back():
    data = request.get_json()
    return jsonify({"message": data})

@jsonify_bp.route('/format', methods=['POST'])
def format_data():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    return jsonify({"message": f"Name: {name}, Age: {age}"})
