from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# Initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the database with the app
    db.init_app(app)

    # Import blueprints and register them
    from app.routes_practice import routes_bp
    from app.jsonify_practice import jsonify_bp
    from app.validation_practice import validation_bp
    from app.user_management import user_bp

    app.register_blueprint(routes_bp, url_prefix='/routes')
    app.register_blueprint(jsonify_bp, url_prefix='/jsonify')
    app.register_blueprint(validation_bp, url_prefix='/validation')
    app.register_blueprint(user_bp, url_prefix='/user')

    return app
