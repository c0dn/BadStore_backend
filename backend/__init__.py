from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from .config import config

app = Flask(__name__)
app.config.from_object(config['dev'])
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access", "refresh"]


app.url_map.strict_slashes = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

api = Api(app, version="1.0", title="Bad Store Backend", doc="", add_specs=False)

from backend.Auth_api import api as auth_api
from backend.Product_api import api as product_api
from backend.Cart_api import api as cart_api

api.add_namespace(auth_api)
api.add_namespace(product_api)
api.add_namespace(cart_api)
