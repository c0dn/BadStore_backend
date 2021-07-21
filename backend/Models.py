import datetime
import random

from backend import db
from backend import bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    # orders = db.relationship("Order", backref="user", lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    retail_price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text(500), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    pic_filename = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.retail_price}', '{self.stock}')"

# class Order(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     order_date = db.Column(db.String(100), nullable=False)
#     total_price = db.Column(db.DECIMAL, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
#     items = db.relationship("OrderedProduct", backref="order", lazy=True)
#     tracking_no = db.Column(db.String(30), nullable=True, default=None)
#     confirm_received = db.Column(db.Boolean, nullable=False, default=False)
#     address_id = db.Column(db.Integer, db.ForeignKey("address.id", ondelete='SET NULL'), nullable=True)
#
#     def __repr__(self):
#         return f"Order('{self.id}', '{self.order_date}','{self.total_price}','{self.user_id}'')"
