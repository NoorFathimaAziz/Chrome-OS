from flask import Blueprint, request, jsonify
from src.handlers import ListNotifi
from src.handlers import GetNotifi
from src.handlers import DeleteNotifi
from src.handlers import Patchnotifi
from src.handlers import Updatenotifi



notifi_bl = Blueprint("notifi", __name__)


# LIST :
@notifi_bl.route('/list', methods=['GET'])
def notifi_list():
   
    list_params = {
        'orderBy': request.json.get('orderBy'),
        'language': request.json.get('language'),
        'pageToken': request.json.get('pageToken'),
        'maxresults' : request.json.get('maxresults')
    }
    # Remove None values and process request
    list_params = {k: v for k, v in list_params.items() if v is not None}
    result = ListNotifi().list(**list_params)
    # Return appropriate response
    return (
        jsonify(result.get('data', {})), 200
    )


# GET:
@notifi_bl.route('/get',methods = ['GET'])
def get_notifi():
    customer = request.args['customer']
    notificationId = request.args['notificationId']
    return GetNotifi().get().execute()


# DELETE:
@notifi_bl.route('/delete', methods=['GET'])
def delete_notifi():
        customer = request.args['customer']
        notificationId = request.args['notificationId']
        # return DeleteNotifi().delete(customer,notificationId)
        response = DeleteNotifi().delete(customer,notificationId)
        return jsonify(response),200


# PATCH :
@notifi_bl.route('/patch',methods=['POST'])
def patchnotifi():
    return Patchnotifi().patch(request.json)


# UPDATE :
@notifi_bl.route('/update',methods=['POST'])
def updatenotifi():
    return Updatenotifi().update(request.json)


