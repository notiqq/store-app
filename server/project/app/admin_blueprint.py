import os

from flask import Blueprint, jsonify, request, render_template, redirect

from project.entities.product import Product
from project import db


admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin', methods=['GET'])
def product_list():
    products = [product.to_json() for product in Product.query.all()]
    return render_template("pages/admin/product/index.html", products=products)

@admin_blueprint.route('/admin/product/add', methods=['GET','POST'])
def product_add():

    if request.method == 'POST':
        post_data = request.get_json()
        name = post_data.get('name')
        price = post_data.get('price')
        image_url = post_data.get('image_url')
        db.session.add(Product(name=name, price=price, image_url=image_url))
        db.session.commit()
        return redirect("/admin", code=303)
    
    return render_template("pages/admin/product/add.html")

@admin_blueprint.route('/admin/product/edit/<product_id>', methods=['GET','POST'])
def product_edit(product_id):
  
    product = Product.query.filter_by(id=product_id).first()
    if request.method == 'GET':
        return render_template("pages/admin/product/edit.html")

    if request.method == 'POST':
        post_data = request.get_json()
        product.name = post_data.get('name')
        product.price = post_data.get('price')
        product.image_url = post_data.get('image_url')
        db.session.commit()
    return redirect("/admin", code=303)

@admin_blueprint.route('/admin/product/delete/<product_id>', methods=['GET'])
def product_delete(product_id):

    product = Product.query.filter_by(id=product_id).first()
    if product == None:
        return redirect("/admin", code=303)
    db.session.delete(product)
    db.session.commit()
    return redirect("/admin", code=303)


if __name__ == '__main__':
    app.run()