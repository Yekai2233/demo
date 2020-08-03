from flask import jsonify, request
import requests
from common.route import Router
from settings import SERVICE

auth_router = Router('auth')


@auth_router.route('/<re(r".*"):path>', methods=["GET", "POST", "PUT", "DELETE"])
def index(path):
    path_key = path.split('/')[0]
    url = "http://127.0.0.1:{}/v1/".format(SERVICE[path_key]['port']) + path
    if request.method == "GET":
        res = requests.get(url)
        return jsonify(res.json())
    elif request.method == "POST":
        res = requests.post(url, data=request.data)
        return jsonify(res.json())
    elif request.method == "PUT":
        res = requests.put(url, data=request.data)
        return jsonify(res.json())
    elif request.method == "DELETE":
        res = requests.delete(url, data=request.data)
        return jsonify(res.json())
    else:
        return jsonify({'code': 404, "msg": {"path": path, "method": request.method}})


@auth_router.route('/login', methods=['GET'])
def login():
    return jsonify({'code': 200, "msg": "login"})


@auth_router.route('/login_out', methods=['GET'])
def login_out():
    return jsonify({'code': 200, "msg": "logout"})
