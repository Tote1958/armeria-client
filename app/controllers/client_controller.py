from flask import Blueprint, jsonify, request
from app.services.client_service import ClientService
from ..mapping.client_schema import ClientSchema


service = ClientService()
client_schema_many = ClientSchema(many=True) # es para que devuelva varios objetos, este se usa para find_all
client_schema = ClientSchema()
client = Blueprint('client', __name__)


@client.route('/client/', methods=['GET'])
def index():
    list = service.find_all()
    result = client_schema_many.dump(list)
    resp = jsonify(result)
    resp.status_code = 200
    return resp


@client.route('/client/id/<int:id>', methods=['GET'])
def find_by_id(id):
    response = client_schema.dump(service.find_by_id(id))
    resp = jsonify(response)
    resp.status_code = 200
    return resp




@client.route('/client/create/', methods=['POST'])
def create_client():
    client = client_schema.load(request.json)
    response = client_schema.dump(service.create(client))
    resp = jsonify(response)
    resp.status_code = 200
    return resp


@client.route('/client/name/', methods=['GET'])
def find_by_name():
    name = request.args.get('name')

    response = client_schema_many.dump(service.find_by_name(name))
    resp = jsonify(response)
    resp.status_code = 200
    return resp
    if response:
        response_builder.add_message("Nombre encontrado").add_status_code(100).add_data({'clients': response})



@client.route('/client/email/<string:email>', methods=['GET'])
def find_by_email(email):
    response = client_schema.dump(service.find_by_email(email))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@client.route('/client/update/<int:id>', methods=['PUT'])
def update_client(id):
    client = request.json
    response = client_schema.dump(service.update(client, id))
    resp = jsonify(response)
    resp.status_code = 200
    return resp



@client.route('/client/delete/<int:id>', methods=['DELETE'])
def delete_client(id):
    response = client_schema.dump(service.delete(id))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

    