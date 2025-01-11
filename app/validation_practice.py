from flask import Blueprint, request, jsonify

validation_bp = Blueprint('validation_bp', __name__)

def validate_json(data):
    if 'name' not in data or 'age' not in data:
        return False
    return True

@validation_bp.route('/data', methods=['POST'])
def handle_data():
    data = request.get_json()

    if not data or not validate_json(data):
        return jsonify({"error": "Invalid data format"}), 400

    return jsonify({"message": "Data received successfully"}), 200
