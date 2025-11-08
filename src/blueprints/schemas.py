from flask import request,Blueprint,jsonify
from src.handlers import SchemaList,SchemaAdd,SchemaGet,SchemaUpdate,SchemaPatch,SchemaDelete

schema_bl = Blueprint('schema',__name__)

@schema_bl.route('/list',methods=['GET'])
def list_schema():
    return SchemaList().handle()

@schema_bl.route('/add',methods=['POST'])
def add_schema():
    return SchemaAdd().handle(request.json)

@schema_bl.route('get',methods=["GET"])
def get_schema():
    schemaKey = request.args['schemaKey']
    return SchemaGet().handle(schemaKey)


@schema_bl.route('/update', methods=['POST'])
def update_schema():
        data = request.get_json()
        response = SchemaUpdate().handle(data)
        return jsonify(response), 200


@schema_bl.route('/patch', methods=['POST'])
def patch_schema():
        data = request.get_json()
        response = SchemaPatch().handle(data)
        return jsonify(response), 200

@schema_bl.route('/delete', methods=['GET'])
def delete_schema():
        schemaKey = request.args.get('schemakey')
        response = SchemaDelete().handle(schemaKey)
        return jsonify(response), 200 