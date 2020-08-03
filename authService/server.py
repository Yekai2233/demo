from flask import Flask

from settings import AUTH_PORT


def register_blueprints(app):
    from common.route import RegexConverter
    app.url_map.converters['re'] = RegexConverter

    from authService.route import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    register_blueprints(app)
    return app


app = create_app()

if __name__ == '__main__':

    app.run(port=AUTH_PORT)

