from flask import Blueprint, request,jsonify
from src.handlers import GroupList,GroupAdd,GroupGet,GroupUpdate,GroupPatch,GroupDelete,AliasListGroup,AliasAddGroup,AliasDeleteGroup

group_bl = Blueprint("group", __name__)

@group_bl.route('/list', methods=['POST'])
def list_group():
   
    list_params = {
        'orderBy': request.json.get('orderBy'),
        'domain': request.json.get('domain'),
        'query': request.json.get('query'),
        'pageToken': request.json.get('pageToken'),
        'sortOrder': request.json.get('sortOrder'),
        'maxResults': request.json.get('maxResults'),
    }

    # Remove None values and process request
    list_params = {k: v for k, v in list_params.items() if v is not None}
    result = GroupList.list_group(**list_params)

    # Return appropriate response
    return (
        jsonify(result.get('data', {})), 200
    )

@group_bl.route('/add',methods=['POST'])
def add_group():
    return GroupAdd().handle(request.json)


@group_bl.route('/get',methods =['GET'])
def get_group():
    groupKey= request.args['groupkey'] 
    return GroupGet().handle(groupKey)

@group_bl.route('/update', methods=['POST'])
def update_group():
        data = request.get_json()
        response = GroupUpdate().handle(data)
        return jsonify(response), 200


@group_bl.route('/patch', methods=['POST'])
def patch_group():
        data = request.get_json()
        response = GroupPatch().handle(data)
        return jsonify(response), 200

@group_bl.route('/delete', methods=['GET'])
def delete_group():
        groupKey = request.args.get('groupkey')
        response = GroupDelete().handle(groupKey)
        return jsonify(response), 200

@group_bl.route('/aliaslist', methods=['GET'])
def list_Alias():
    groupKey = request.args.get('groupkey')
    return AliasListGroup().handle(groupKey) 


@group_bl.route('/aliasadd',methods=['POST'])
def addalias_group():
    return AliasAddGroup().handle(request.json)

@group_bl.route('/deletealias', methods=['POST'])
def delete_alias():
    # Get JSON body from request
    body = request.get_json()

    # Validate request body
    if not body:
        return jsonify({"error": "Request body is empty"}), 400

    # Validate required fields
    if 'groupKey' not in body or 'alias' not in body:
        return jsonify({"error": "Both groupKey and alias are required"}), 400

    # Create AliasDeleteHandler instance and handle deletion
    alias_delete_handler = AliasDeleteGroup()
    response, status_code = alias_delete_handler.handle(body)
    
    return jsonify(response), status_code

