from sys import prefix

from flask import request, Blueprint, jsonify
from repository.init_repository import init_traffic_crashes

init_blueprint = Blueprint('init_blueprint', __name__)


@init_blueprint.route('/', methods=['GET'])
def init_bp():
    success = init_traffic_crashes()
    return jsonify({'message': 'db initialized successfully'}), 200

