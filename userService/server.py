from flask import Flask, jsonify
from settings import USER_PORT


def register_blueprints(app):
    from userService.route import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    register_blueprints(app)
    return app


app = create_app()

if __name__ == '__main__':

    app.run(port=USER_PORT)
