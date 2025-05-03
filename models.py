from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    wishlists = db.relationship('Wishlist', backref='creator', lazy=True)
    products_added = db.relationship('Product', backref='added_by', lazy=True)

class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    products = db.relationship('Product', backref='wishlist', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)
    wishlist_id = db.Column(db.Integer, db.ForeignKey('wishlist.id'), nullable=False)
    added_by_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    wishlist = db.relationship('Wishlist', backref=db.backref('products', lazy=True))
    added_by = db.relationship('User', backref=db.backref('products_added', lazy=True))
