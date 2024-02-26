from app.main import bp as app
from flask import request, jsonify

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    print(data)
    
    return jsonify({'message': ''}), 200