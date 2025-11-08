from flask import Blueprint, request
from src.handlers import OrganizationList, OrganizationGet,OrganizationAdd,OrganizationUpdate,OrganizationUpdatePatch,OrganizationDelete

org_bl = Blueprint("organizations", __name__)

@org_bl.route('/list', methods=['GET'])
def list_org_units():
    type_param = request.args.get('type', 'children')
    return OrganizationList().handle(type_param)


@org_bl.route('/get', methods=['GET'])
def get_org_units():
    orgUnitPath = request.args['orgUnitPath']
    return OrganizationGet().handle(orgUnitPath)

@org_bl.route('/add',methods=['POST'])
def add_org_units(): 
    return OrganizationAdd().handle(request.json)

@org_bl.route('/update', methods=['POST'])
def update_org_units():
    return OrganizationUpdate().handle(request.json)

@org_bl.route('/patch', methods=['POST'])
def update_patch_org_units():
    return OrganizationUpdatePatch().handle(request.json)

@org_bl.route('/delete', methods=['GET'])
def delete_org_units():
    orgUnitPath = request.args['orgUnitPath']
    return OrganizationDelete().handle(orgUnitPath)




