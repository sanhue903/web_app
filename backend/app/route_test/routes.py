from app.route_test import bp as app
from flask import jsonify, request

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Hello World"}), 200