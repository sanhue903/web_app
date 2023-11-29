from app.auth import bp as app
from app.extensions import db

@app.route('/login', methods=['GET'])
def login():
    return 'login'

@app.route('/logout', methods=['GET'])
def logout():
    return 'logout'

@app.route('/signup', methods=['GET'])
def signup():
    return 'signup'
