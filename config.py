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
    DATABASE_USER = os.environ.get("DATABASE_USER") or "postgres"
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD") or ""
    DATABASE_NAME = os.environ.get("DATABASE_NAME") or "dev_manga"
    DATABASE_HOST = os.environ.get("DATABASE_HOST") or "127.0.0.1"
    DATABASE_PORT = os.environ.get("DATABASE_PORT") or "5432"
    CONNECTION_STR = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DEV_DATABASE_URI") or CONNECTION_STR


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
