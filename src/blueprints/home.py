from flask import Blueprint

home_bl = Blueprint("home", __name__)

@home_bl.route('/', methods=['GET'])
def home():
    return "hi i am a server"