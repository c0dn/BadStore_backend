import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    APP_NAME = "Backend for Bad Store"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "5791628bb0b13ce0c676dfde280ba245"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    PAGINATE_MAX_SIZE = 20
    PAGINATE_PAGE_SIZE = 10


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "test.db")


class ProdConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "prod.db")


config = {
    "dev": DevConfig,
    "prod": ProdConfig,
    "default": DevConfig
}
