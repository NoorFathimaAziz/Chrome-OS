from flask import Blueprint, request, jsonify
from src.handlers import ChromeList 
from src.handlers import ChromeOSget
from src.handlers import ActionHandler
from src.handlers import PatchChrome
from src.handlers import UpdateChrome
from src.handlers import MoveChromeOS


chrome_bl = Blueprint("chrome", __name__)
 
@chrome_bl.route('/list', methods=['POST'])
def list_chrome():
   
    list_params = {
        'orderBy': request.json.get('orderBy'),  
        'projection': request.json.get('projection'),
        'query': request.json.get('query'),
        'pageToken': request.json.get('pageToken'),
        'sortOrder': request.json.get('sortOrder'),
        'maxResults': request.json.get('maxResults'),
        'orgunitpath': request.json.get('orgunitpath')
    }
 
    # Remove None values and process request
    list_params = {k: v for k, v in list_params.items() if v is not None}
    result = ChromeList.list_chrome(**list_params)
 
    # Return appropriate response
    return (
        jsonify(result.get('data', {})), 200
    )


# # GET chromeosdevice:
@chrome_bl.route('/get', methods=['GET'])
def get_chromos():
    deviceId = request.args.get('deviceId')
    return ChromeOSget().chromehandle(deviceId)


# MOVEDEVICES/INSERT CHROMEOSDEVICES:
@chrome_bl.route('/move', methods=['POST'])
def movechrome():
    return MoveChromeOS().move(request.json)


# PATCH CHROMEOSDEVICES:
@chrome_bl.route('/patch', methods=['POST'])
def patch_chromeos():
    return PatchChrome().patch(request.json)


# UPDATE CHROMEOSDEVICES:

@chrome_bl.route('/update', methods=['POST'])
def update_chromeos():
    return UpdateChrome().update(request.json)


# # ACTION chromosdevice:
# @chrome_bl.route('/action', methods=['POST'])
# def action_chromeos():
#     return ActionHandler().chromeaction(request.json)

@chrome_bl.route('/action', methods=['POST'])
def action_chromeos():
    return ActionHandler().chromeaction(request.json)






