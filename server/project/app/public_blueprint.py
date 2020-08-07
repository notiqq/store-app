import os

from flask import Blueprint, jsonify, request, render_template

from project.entities.product import Product
from project import db


public_blueprint = Blueprint('public', __name__)

@public_blueprint.route('/', methods=['GET'])
def home():
    products = [product.to_json() for product in Product.query.limit(4).all()]
    return render_template("pages/public/index.html", products=products)

@public_blueprint.route('/public/all', methods=['GET'])
def get_all():
    response_object = [product.to_json() for product in Product.query.all()]
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()