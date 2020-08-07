from flask.cli import FlaskGroup

from project import create_app, db
from project.entities.product import Product


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
        name='FLORAL JACKQUARD PULLOVER',
        price= '120.00',
        image_url='static/public/images/product-1.jpg'
    ))
    db.session.add(Product(
        name='CUTE JACKQUARD DRESS',
        price='200.00',
        image_url='static/public/images/product-2.jpg'
    ))
    db.session.add(Product(
        name='CUTE JACKQUARD SKIRT',
        price='508.00',
        image_url='static/public/images/product-3.jpg'
    ))
    db.session.add(Product(
        name='CUTE JACKQUARD PULLOVER',
        price='320.00',
        image_url='static/public/images/product-4.jpg'
    ))
    db.session.commit()


if __name__ == '__main__':
    cli()