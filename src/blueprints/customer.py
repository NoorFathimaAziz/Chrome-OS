from flask import Blueprint,request
from src.handlers import CustomerGet,CustomerUpdate,CustomerPatch

cus_bl = Blueprint("customer", __name__)

@cus_bl.route('/get', methods=['GET'])
def get_customer():
    return CustomerGet().handle()

@cus_bl.route('/update', methods=['POST'])
def update_customer():
    return CustomerUpdate().handle(request.json)

@cus_bl.route('/patch',methods=['POST'])
def patch_customer():
    return CustomerPatch().handle(request.json)