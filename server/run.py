from flask.cli import FlaskGroup

from project import create_app, db
from project.app.models import Product


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(Product(
        name='Apple iPhone 11 Pro Max',
        price= '1099',
        image_url='https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-pro-max-space-select-2019?wid=834&hei=1000&fmt=jpeg&qlt=95&op_usm=0.5,0.5&.v=1566953858806'
    ))
    db.session.add(Product(
        name='Apple iPhone 7',
        price='200',
        image_url='https://cdn.movertix.com/media/catalog/product/cache/image/1200x/a/p/apple-iphone-7-en-negro-mate-de-32gb-detras.jpg'
    ))
    db.session.add(Product(
        name='Apple iPhone XS',
        price='508',
        image_url='https://stylus.ua/thumbs/390x390/c2/24/839696.jpeg'
    ))
    db.session.commit()


if __name__ == '__main__':
    cli()