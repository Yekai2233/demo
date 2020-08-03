from flask import Blueprint

from userService import views


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    views.user_router.register(bp_v1)

    return bp_v1


