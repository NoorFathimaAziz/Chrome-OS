from flask import Blueprint, request
from src.handlers import DomainList,DomainAdd,DomainGet,DomainDelete

domain_bl = Blueprint("domain", __name__)

@domain_bl.route('/list', methods=['GET'])
def list_domain():
    return DomainList().handle()

@domain_bl.route('/add',methods=['POST'])
def add_domain():
    return DomainAdd().handle(request.json)


@domain_bl.route('/get', methods=['GET'])
def get_domain():
    domainName = request.args['domainName']
    return DomainGet().handle(domainName)

@domain_bl.route('/delete', methods=['GET'])
def delete_domain():
    domainName = request.args['domainName']
    return DomainDelete().handle(domainName)

