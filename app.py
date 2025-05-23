from flask import Flask
from routes.livros import livros_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(livros_bp)
    return app




