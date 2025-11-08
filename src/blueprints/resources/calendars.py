from flask import Blueprint, request, jsonify
from src.handlers import CalList
from src.handlers import CalAdd
from src.handlers import CalGet
from src.handlers import CalDel
from src.handlers import CalUpdate
from src.handlers import CalPatch




cal_bl = Blueprint("calendar", __name__)

@cal_bl.route('/list', methods=['GET'])
def list_cal():
   
    list_params = {
        'orderBy' :request.args.get('orderBy'),
        'pageToken': request.args.get('pageToken'),
        'maxResults': request.args.get('maxResults'),
        'query' : request.args.get('query')
    }

    # Remove None values and process request
    list_params = {k: v   for k, v in list_params.items() if v is not None}
    result = CalList.list(**list_params)

    # Return appropriate response
    return (
        jsonify(result.get('data', {})), 200
    )


# INSERT
@cal_bl.route('/insert',methods=['POST'])
def add_cal():
    return CalAdd().caladd(request.json)


# GET
@cal_bl.route('/get',methods =['GET'])
def get_cal():
    calendarResourceId= request.args['calendarResourceId']
    return CalGet().calget(calendarResourceId)


# delete
@cal_bl.route('/delete', methods=['GET'])
def delete_cal():
        calendarResourceId = request.args.get('calendarResourceId')
        response = CalDel().cal_del()
        return jsonify(response), 200


# UPDATE
@cal_bl.route('/update', methods=['POST'])
def update_cal():
    return CalUpdate().cal_update(request.json)


# PATCH
@cal_bl.route('/patch', methods=['POST'])
def patch_cal():
        # data = request.get_json()
        # response = UserPatch().handle(data)
    return CalPatch().cal_patch(request.json)




























