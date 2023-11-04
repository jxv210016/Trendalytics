from flask import Blueprint, jsonify

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "API is running"}), 200
