from flask import Blueprint

bp = Blueprint('auth', __name__)
from app.core import bp as core_bp
bp.register_blueprint(core_bp)

from app.auth import forms, routes
