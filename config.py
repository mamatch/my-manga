import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    The base configuration of the application
    """
    SECRET_KEY = os.environ.get("SECRET_KEY") or "Djoum@tchou@95"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DEV_DATABASE_URI") or f"sqlite:///{os.path.join(basedir, 'data-dev.sqlite')}"


class TestConfig(Config):
    pass


class ProdConfig(Config):
    pass


config = {
    "dev": DevConfig,
    "test": TestConfig,
    "prod": ProdConfig,
    "default": DevConfig,
}
