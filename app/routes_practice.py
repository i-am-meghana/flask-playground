from flask import Blueprint, request, jsonify

routes_bp = Blueprint('routes_bp', __name__)

@routes_bp.route('/notes')
def index():
    return "hello"

@routes_bp.route('/notes/<int:notes_id>')
def note(notes_id):
    return f"hello id number {notes_id}"

@routes_bp.route('/handling_url_parameters')
def handling_parameters():
    return str(request.args)

@routes_bp.route('/handle_url_parameters')
def handle_parameters():
    if 'greeting' in request.args and 'name' in request.args:
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f'{greeting} {name}'
    return 'Some parameters are missing'

@routes_bp.route('/greet/<int:user_id>')
def greeting(user_id):
    name = request.args.get('name', 'Guest')
    age = request.args.get('age', 'none')
    return jsonify(f'Hello {name}{user_id} of age {age}')

@routes_bp.route('/post/<int:post_id>/comment/', methods=['GET'])
@routes_bp.route('/post/<int:post_id>/comment/<int:comment_id>', methods=['GET'])
def show_comment(post_id, comment_id=None):
    comment_id = request.args.get('comment_id', comment_id or 1, type=int)
    return f'Post ID: {post_id}, Comment ID: {comment_id}'

@routes_bp.route('/product/<int:product_id>', defaults={'comment_id': 0})
@routes_bp.route('/product/<int:product_id>/comment/<int:comment_id>')
def show_product(product_id, comment_id):
    return f'product ID: {product_id}, Comment ID: {comment_id}'


data_store = []
@routes_bp.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()#convert the JSON into a Python dictionary. request contains the data sent by the client
    data_store.append(data)#will add this dictionary to the data_store list
    #Before: data_store = []
    #After: data_store = [{"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"}]
    return jsonify({"message": "Data submitted successfully", "data": data}), 201