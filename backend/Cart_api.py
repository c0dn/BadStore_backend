from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required

api = Namespace("cart", description="Cart related")


@api.route("/checkout/")
class CartCheckout(Resource):

    @jwt_required()
    def post(self):
        response_obj = {
            "success": True,
        }
        return response_obj
