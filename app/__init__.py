# app/__init__.py

from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()


def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(settings_module)

    # Load the configuration from the folder instance:
    if app.config.get('TESTING', False):
        app.config.from_pyfile('config-testing.py', silent=True)
    else:
        app.config.from_pyfile('config.py', silent=True)

    login_manager.init_app(app)
    login_manager.login_view = "public.index"

    db.init_app(app)
    migrate.init_app(app, db)
    
    # Registro de los blueprints:
    from .public import public_bp
    app.register_blueprint(public_bp)

    register_error_handlers(app)

    return app

def register_error_handlers(app):
    @app.errorhandler(500)
    def error_handler_500(err):
        return render_template("500.html"), 500

    @app.errorhandler(404)
    def error_handler_404(err):
        return render_template("404.html"), 404

    @app.errorhandler(401)
    def error_handler_401(err):
        return render_template("401.html"), 401