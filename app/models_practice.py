from flask import Blueprint, jsonify, request
from app import db
from app.models import User,Book  # assuming you have a User model defined

models_bp = Blueprint('models_bp', __name__)


@models_bp.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'], genre=data['genre'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book created"}), 201

@models_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    result = [{"id": book.id, "title": book.title, "author": book.author, "genre": book.genre} for book in books]
    return jsonify(result)


# Create a view function that inserts a new record into the User table.
@models_bp.route('/create', methods=['POST'])#endpoint
def create_user():#view function
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({"message": "Name and email are required!"}), 400

    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": f"User {name} added successfully!"}), 201

    """ retrieve all users from the database.
        Use Postman to send a GET request to retrieve the user data.
    """
@models_bp.route('/user')
def user_data():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])