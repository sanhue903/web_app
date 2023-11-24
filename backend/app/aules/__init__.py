from flask import Blueprint

bp = Blueprint('aules', __name__)

from app.aules import routes