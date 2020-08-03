from flask import Blueprint

from authService.views import auth_router


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    auth_router.register(bp_v1)

    return bp_v1
