import os

from flask import Blueprint, jsonify, request, render_template

from project.app.models import Product
from project import db


admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin', methods=['GET'])
def home():
    products = [product.to_json() for product in Product.query.all()]
    return render_template("pages/admin/index.html", products=products)

if __name__ == '__main__':
    app.run()