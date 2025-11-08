from flask import Blueprint, request , jsonify
from src.handlers import ListMobDevices
from src.handlers import GetMobdevices
from src.handlers import DelMobdevices
from src.handlers import ActionMobDevices
 
mobdevices_bl = Blueprint("mobdevices", __name__)
 
@mobdevices_bl.route('/list', methods=['POST'])
def list_mobile():
   
    list_params = {
        'orderBy': request.json.get('orderBy'),
        'projection': request.json.get('projection'),
        'query': request.json.get('query'),
        'pageToken': request.json.get('pageToken'),
        'sortOrder': request.json.get('sortOrder'),
        'maxResults': request.json.get('maxResults'),
    }
 
    # Remove None values and process request
    list_params = {k: v for k, v in list_params.items() if v is not None}
    result = ListMobDevices.list_mobile(**list_params)
 
    # Return appropriate response
    return (
        jsonify(result.get('data', {})), 200
    )


# # GET MOBDEVICES:
# @mobdevices_bl.route('/get',methods=['GET'])
# def getmob():
#     resourceId = request.args.get['resourceId']
#     return GetMobdevices().get(resourceId)


@mobdevices_bl.route('/get',methods=['POST'])
def getmob():
    # resourceId = request.json.get['resourceId']
    return GetMobdevices().get(request.json)



# DELETE MOBDEVICES:
@mobdevices_bl.route('/delete',methods=['GET'])
def deletemob():
    customerId = request.args.get('customerId')
    # resourceId = request.args.get('resourceId')
    resourceId = request.args['resourceId']
    response = DelMobdevices().delete(customerId,resourceId)
    return jsonify(response), 200


@mobdevices_bl.route('/action',methods=['POST'])
def action():
    return ActionMobDevices().action(request.json)