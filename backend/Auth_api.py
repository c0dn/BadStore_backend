import datetime
import json

from flask import request, make_response, jsonify, url_for, session, redirect
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_restx import Namespace, Resource
from backend import db, bcrypt
from backend.Models import User

api = Namespace("auth", description="Auth related")


@api.route("/login/")
class Login(Resource):

    def post(self):
        post_data = request.get_json()
        email = post_data.get("email")
        password = post_data.get("password")
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.id, expires_delta=datetime.timedelta(days=300))
            return {"success": True, "access_token": access_token}
        else:
            response_obj = {
                "success": False,
                "message": "Incorrect username or password",
            }
            return response_obj, 401
