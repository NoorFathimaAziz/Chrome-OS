from flask import Flask
from src.blueprints import reg_blueprints

def create_app():
    app = Flask(__name__)
    reg_blueprints(app)
    return app

