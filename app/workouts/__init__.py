from flask import Blueprint

workouts_bp = Blueprint('workouts', __name__, url_prefix='/workouts')

from . import routes