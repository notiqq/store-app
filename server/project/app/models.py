import datetime

from flask import current_app
from sqlalchemy.sql import func

from project import db


class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
   

    def __init__(self, name, price, image_url):
        self.name = name
        self.price = price
        self.image_url = image_url

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'image_url': self.image_url
        }
