# app/__init__.py

from flask import Flask


def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    # Registro de los blueprints:
    from .public import public_bp
    app.register_blueprint(public_bp)

    return app