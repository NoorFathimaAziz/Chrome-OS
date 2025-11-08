from flask import Blueprint,request
from src.handlers import verificationList,verificationInvaild,verificationGenerate

verification_bl = Blueprint("verification", __name__)

@verification_bl.route('/list', methods=['GET'])
def list_verification():
    userKey = request.args['userKey']
    return verificationList().handle(userKey)


@verification_bl.route('/invalid', methods=['GET'])
def invaild_verification():
    userKey = request.args['userKey']
    return verificationInvaild().handle(userKey)


@verification_bl.route('/generate', methods=['GET'])
def generate_verification():
    userKey = request.args['userKey']
    return verificationGenerate().handle(userKey)
