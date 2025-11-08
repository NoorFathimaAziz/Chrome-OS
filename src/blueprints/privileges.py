from flask import Blueprint, request, jsonify
from src.handlers import Listpriv

priv_bl= Blueprint("priv", __name__)

@priv_bl.route('/list', methods=['GET'])
def listpriv():
   return Listpriv().list()