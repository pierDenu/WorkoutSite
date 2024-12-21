from flask import Blueprint

plans_bp = Blueprint('plans', __name__, url_prefix='/plans')

from . import routes