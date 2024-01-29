from flask import Flask
from app.routes import student_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(student_bp)
    return app
