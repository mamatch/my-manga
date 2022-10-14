from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()
moment = Moment()
boots = Bootstrap()
mail = Mail()


def create_app(config_name: str) -> Flask:
    """
    A function to create a flask application instance
    :param config_name: the configuration to load from the config.py ("dev","test","prod","default")
    :return: app: The flask app instance
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    boots.init_app(app)
    mail.init_app(app)
    moment.init_app(app)

    # TODO: Add routes and blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
