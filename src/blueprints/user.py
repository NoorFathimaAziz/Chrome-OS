from flask import Blueprint, request, jsonify
from src.handlers import UserListHandler,UserAdd,UserGet,UserPatch,UserDelete,UserUndelete,UserUpdate,MakeAdmin,AliasAdd,AliasList,AliasDelete,PhotoGet,PhotoDelete,PhotoPatch,PhotoUpdate

user_bl = Blueprint("user", __name__)

@user_bl.route('/list', methods=['POST'])
def list_user():
   
    list_params = {
        'orderBy': request.json.get('orderBy'),
        'domain': request.json.get('domain'),
        'projection': request.json.get('projection'),
        'query': request.json.get('query'),
        'event': request.json.get('event'),
        'showDeleted': request.json.get('showDeleted'),
        'pageToken': request.json.get('pageToken'),
        'sortOrder': request.json.get('sortOrder'),
        'maxResults': request.json.get('maxResults'),
        'customFieldMask': request.json.get('customFieldMask'),
        'viewType': request.json.get('viewType')
    }

    # Remove None values and process request
    list_params = {k: v   for k, v in list_params.items() if v is not None}
    result = UserListHandler.list_users(**list_params)

    # Return appropriate response
    return (
        jsonify(result.get('data', {})), 200
    )

@user_bl.route('/add',methods=['POST'])
def add_user():
    return UserAdd().handle(request.json)

@user_bl.route('/get',methods =['GET'])
def get_user():
    userKey= request.args['userkey']
    return UserGet().handle(userKey)

@user_bl.route('/update', methods=['POST'])
def update_user():
        data = request.get_json()
        response = UserUpdate().handle(data)
        return jsonify(response), 200

@user_bl.route('/patch', methods=['POST'])
def patch_user():
        data = request.get_json()
        response = UserPatch().handle(data)
        return jsonify(response), 200

@user_bl.route('/delete', methods=['GET'])
def delete_user():
        userKey = request.args.get('userkey')
        response = UserDelete().handle(userKey)
        return jsonify(response), 200


@user_bl.route('/undelete', methods=['POST'])
def undelete_user():
        data = request.get_json()
        response = UserUndelete().handle(data)
        return jsonify(response), 200
    
@user_bl.route('/makeadmin',methods =['POST'])
def makeadmin_user():
      data = request.get_json()
      response = MakeAdmin().handle(data)
      return jsonify(response),200

@user_bl.route('/aliaslist', methods=['GET'])
def list_Alias():
    userKey = request.args.get('userkey')
    return AliasList().handle(userKey) 

@user_bl.route('/aliasadd',methods=['POST'])
def addalias_user():
    return AliasAdd().handle(request.json)

@user_bl.route('/deletealias', methods=['POST'])
def delete_alias():
    # Get JSON body from request
    body = request.get_json()

    # Validate request body
    if not body:
        return jsonify({"error": "Request body is empty"}), 400

    # Validate required fields
    if 'userKey' not in body or 'alias' not in body:
        return jsonify({"error": "Both userKey and alias are required"}), 400

    # Create AliasDeleteHandler instance and handle deletion
    alias_delete_handler = AliasDelete()
    response, status_code = alias_delete_handler.handle(body)
    
    return jsonify(response), status_code


@user_bl.route('/get',methods =['GET'])
def get_photo():
    userKey= request.args['userkey']
    return PhotoGet().handle(userKey)


@user_bl.route('/update', methods=['POST'])
def update_photo():
        data = request.get_json()
        response = PhotoUpdate().handle(data)
        return jsonify(response), 200

@user_bl.route('/patch',methods =['POST'])
def patch_photo():
     data = request.get_json()
     response = PhotoPatch().handle(data)
     return jsonify(response),200


@user_bl.route('/delete', methods=['GET'])
def delete_photo():
        userKey = request.args.get('userkey')
        response = PhotoDelete().handle(userKey)
        return jsonify(response), 200