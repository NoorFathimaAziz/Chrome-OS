from flask import Blueprint, request, jsonify
from src.handlers import RoleAssList,RoleAssAdd,RoleAssGet,RoleAssDelete

roleass_bl = Blueprint("roleass", __name__)

@roleass_bl.route('/list', methods=['POST'])
def list_roleass():
   
    list_params = {
        'roleId': request.json.get('roleId'),
        'userKey': request.json.get('userKey'),
        'pageToken': request.json.get('pageToken'),
        'maxResults': request.json.get('maxResults'),
        
    }

    # Remove None values and process request
    list_params = {k: v for k, v in list_params.items() if v is not None}
    result = RoleAssList.list_roleass(**list_params)

    # Return appropriate response
    return (
        jsonify(result.get('data', {})), 200
    )

@roleass_bl.route('/add',methods=['POST'])
def add_roleass():
    return RoleAssAdd().handle(request.json)

@roleass_bl.route('/get', methods=['GET'])
def get_roleass():
    roleAssignmentId = request.args['roleAssignmentId']
    return RoleAssGet().handle(roleAssignmentId)

@roleass_bl.route('/delete', methods=['GET'])
def delete_roleass():
        roleAssignmentId = request.args.get('roleAssignmentId')
        response = RoleAssDelete().handle(roleAssignmentId)
        return jsonify(response), 200