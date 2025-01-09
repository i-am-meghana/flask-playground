from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=True)
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique = True, nullable=False)
    
    
    
"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'age': self.age}

    
    
    _task_
    Define a model (e.g., Book) with the following attributes:

    id: Integer (Primary Key)
    title: String
    author: String
    published_date: Date
basic structure, where you define the data types (e.g., Integer, String, Date, etc.) for each column. You can add additional properties such as nullable, default, 
unique, etc., to control how data is handled.

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column
    author
    genre

Implement the following API endpoints:

    POST /books: Add a new book.
    GET /books: Retrieve a list of all books.
    GET /books/<id>: Retrieve a single book by ID.
    PUT /books/<id>: Update the details of a book.
    DELETE /books/<id>: Delete a book by ID.

Test the endpoints using Postman.
    """