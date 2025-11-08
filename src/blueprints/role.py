from flask import Blueprint,request
from src.handlers import RoleGet, RoleList,RoleAdd,RoleUpdate,RolePatch,RoleDelete,List_Next_Role

role_bl = Blueprint("role", __name__)

@role_bl.route('/get', methods=['GET'])
def get_role():
    roleId = request.args['roleId']
    return RoleGet().handle(roleId)

@role_bl.route('/list', methods=['GET'])
def list_roles():
    return RoleList().handle() 

@role_bl.route('/add',methods=['POST'])
def add_role():
    return RoleAdd().handle(request.json)

@role_bl.route('/update', methods=['POST'])
def update_role():
    return RoleUpdate().handle(request.json)

@role_bl.route('/patch',methods = ['POST'])
def patch_role():
    return RolePatch().handle(request.json)

@role_bl.route('/delete', methods=['GET'])
def delete_role():
    roleId = request.args['roleId']
    return RoleDelete().handle(roleId)

@role_bl.route('/list_next',methods = ['POST'])
def list_next_role():
    return List_Next_Role().handle(request.json)
