from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    wishlists = db.relationship('Wishlist', backref='creator', lazy='dynamic')
    products_added = db.relationship('Product', backref='user_added_products', lazy='dynamic')

class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    products = db.relationship('Product', backref='wishlist_association', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)
    wishlist_id = db.Column(db.Integer, db.ForeignKey('wishlist.id'), nullable=False)
    added_by_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)

    wishlist = db.relationship('Wishlist', backref='wishlist_association')
    added_by = db.relationship('User', backref='user_added_products')
