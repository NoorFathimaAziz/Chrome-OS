from flask import Blueprint,request
from src.handlers import PolicySchemaList
from src.handlers import PolicySchemaGet
from src.handlers import PolicySchemaList,PolicySchemaUpdate

policyschema_bl = Blueprint("policy_schema", __name__)


# list
@policyschema_bl.route('/list', methods=['GET'])
def list_policy():
    page_size = request.args.get('page_size', 100)
    next_token =  request.args.get('next_token')
    schema = PolicySchemaList()
    return schema.handle(page_size, next_token)

# GET
@policyschema_bl.route('/get', methods = ['GET'])
def get_policy():
    return PolicySchemaGet().policy_get(request.args.get('schemakey', ''))

# modify
@policyschema_bl.route('/update',methods = ['POST'])
def update_policy():
    return PolicySchemaUpdate().handle(request.json)
