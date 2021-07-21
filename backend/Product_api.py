import os
import uuid
from flask_restx import Namespace, Resource
from werkzeug.utils import secure_filename
from backend.Models import Product, User
from backend import db
from flask import request, make_response, jsonify, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace("products", description="Product related")
UPLOAD_FOLDER = "./backend/uploads/"


@api.route("/uploads/<filename>")
class GetImage(Resource):

    def get(self, filename):
        return send_from_directory(os.path.abspath(UPLOAD_FOLDER), filename)


@api.route("/")
class Products(Resource):

    def get(self):
        products = Product.query.all()
        res = []
        for product in products:
            p = {
                "id": product.id,
                "name": product.name,
                "price": product.retail_price,
                "picture": product.pic_filename,
                "stock": product.stock,
                "description": product.description
            }
            res.append(p)
        return res
