from sys import prefix

from flask import request, Blueprint, jsonify
from repository.init_repository import init_traffic_crashes

init_blueprint = Blueprint('init_blueprint', __name__)


@init_blueprint.route('/', methods=['GET'])
def init_bp():
    success = init_traffic_crashes()
    # if success:
    #     return jsonify({'message': 'db initialized successfully'}), 200
    return jsonify({'message': 'db initial failure'}), 200
