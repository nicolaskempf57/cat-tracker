from flask import Blueprint

bp = Blueprint('errors', __name__)
from app.core import bp as core_bp
bp.register_blueprint(core_bp)

from app.errors import handlers
