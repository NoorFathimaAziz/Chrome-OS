from flask import Blueprint, request, jsonify
from src.handlers import MemberList,MemberAdd,MemberGet,MemberUpdate,MemberPatch,MemberDelete,HasMember

member_bl = Blueprint("member", __name__)

@member_bl.route('/list', methods=['POST'])
def list_member():
   
    list_params = {
        'groupKey': request.json.get('groupKey'),
        'pageToken': request.json.get('pageToken'),
        'roles': request.json.get('roles'),
        'includeDrivedMembership': request.json.get('includeDrivedMembership'),
        'maxResults': request.json.get('maxResults'),
        
    }

    # Remove None values and process request
    list_params = {k: v for k, v in list_params.items() if v is not None}
    result = MemberList.list_member(**list_params)

    # Return appropriate response
    return (
        jsonify(result.get('data', {})), 200
    )

@member_bl.route('/add',methods=['POST'])
def add_Member():
    return MemberAdd().handle(request.json)

@member_bl.route('/get',methods =['GET'])
def get_Member():
    groupKey= request.args['groupKey']
    memberKey = request.args['memberKey']
    return MemberGet().handle(groupKey,memberKey)

@member_bl.route('/update', methods=['POST'])
def update_member():
        data = request.get_json()
        response = MemberUpdate().handle(data)
        return jsonify(response), 200

@member_bl.route('/patch', methods=['POST'])
def patch_member():
        data = request.get_json()
        response = MemberPatch().handle(data)
        return jsonify(response), 200

@member_bl.route('/delete', methods=['GET'])
def delete_member():
        groupKey = request.args.get('groupkey')
        memberKey = request.args.get('memberKey')
        response = MemberDelete().handle(groupKey,memberKey)
        return jsonify(response), 200

@member_bl.route('/hasmember',methods = ['GET'])
def hasmember():
      groupKey = request.args.get('groupKey')
      memberKey = request.args.get('memberKey')
      response = HasMember().handle(groupKey,memberKey)
      return jsonify(response),200  