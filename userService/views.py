from flask import jsonify

from common.route import Router

user_router = Router('user')


@user_router.route('/get_user', methods=['GET'])
def get_user():
    return jsonify({'code': 200, "msg": {"name": "tom", "age": 14}})


@user_router.route('/add_user', methods=['POST'])
def add_user():
    return jsonify({'code': 200, "msg": "add success"})


@user_router.route('/update_user', methods=['PUT'])
def update_user():
    return jsonify({'code': 200, "msg": "update success"})


@user_router.route('/del_user', methods=['PUT'])
def del_user():
    return jsonify({'code': 200, "msg": "del success"})

