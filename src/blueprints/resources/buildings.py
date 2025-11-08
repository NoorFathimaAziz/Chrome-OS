# from flask import Blueprint, request, jsonify
# # from src.handlers import 

# building_bl = Blueprint("building", __name__)

# @building_bl.route('/list', methods=['GET'])
# def list_build():
   
#     list_params = {
#         'pageToken': request.args.get('pageToken'),
#         'maxResults': request.args.get('maxResults'),
#     }

#     # Remove None values and process request
#     list_params = {k: v   for k, v in list_params.items() if v is not None}
#     result = BuildingList.list(**list_params)

#     # Return appropriate response
#     return (
#         jsonify(result.get('data', {})), 200
#     )







# @user_bl.route('/insert',methods=['POST'])
# def add_user():
#     return UserAdd().handle(request.json)

# @user_bl.route('/get',methods =['GET'])
# def get_user():
#     userKey= request.args['userkey']
#     return UserGet().handle(userKey)

# @user_bl.route('/update', methods=['POST'])
# def update_user():
#         data = request.get_json()
#         response = UserUpdate().handle(data)
#         return jsonify(response), 200

# @user_bl.route('/patch', methods=['POST'])
# def patch_user():
#         data = request.get_json()
#         response = UserPatch().handle(data)
#         return jsonify(response), 200

# @user_bl.route('/delete', methods=['GET'])
# def delete_user():
#         userKey = request.args.get('userkey')
#         response = UserDelete().handle(userKey)
#         return jsonify(response), 200

