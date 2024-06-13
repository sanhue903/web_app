from flask import Blueprint

bp = Blueprint('test', __name__)

from app.route_test import routes