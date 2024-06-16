from app.route_test import bp as app
from flask import jsonify, request

@app.route('/test', methods=['GET'])
def test():
    a = 420
    return jsonify(a), 200