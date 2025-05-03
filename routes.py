from flask import request, jsonify
from app import app, db
from models import User, Wishlist, Product

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Wishlist API!"})

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    existing_user = User.query.filter_by(email=data["email"]).first()
    if existing_user:
        return jsonify({"message": "Email already registered"}), 400

    new_user = User(username=data["username"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully!"}), 201

# ✅ Create Wishlist API
@app.route("/wishlist", methods=["POST"])
def create_wishlist():
    data = request.json
    if not data.get("name") or not data.get("creator_id"):
        return jsonify({"message": "Wishlist name and creator ID are required"}), 400

    user = User.query.get(data["creator_id"])
    if not user:
        return jsonify({"message": "User not found"}), 404

    new_wishlist = Wishlist(name=data["name"], creator_id=data["creator_id"])
    db.session.add(new_wishlist)
    db.session.commit()

    return jsonify({"message": "Wishlist created successfully!", "wishlist_id": new_wishlist.id}), 201

# ✅ Retrieve All Wishlists for a User
@app.route("/wishlist/<int:user_id>", methods=["GET"])
def get_wishlists(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    wishlists = Wishlist.query.filter_by(creator_id=user_id).all()
    return jsonify({"wishlists": [{"id": w.id, "name": w.name} for w in wishlists]}), 200

# ✅ Retrieve Items in a Wishlist
@app.route("/wishlist/<int:wishlist_id>/items", methods=["GET"])
def get_wishlist_items(wishlist_id):
    wishlist = Wishlist.query.get(wishlist_id)
    if not wishlist:
        return jsonify({"message": "Wishlist not found"}), 404

    items = Product.query.filter_by(wishlist_id=wishlist_id).all()
    return jsonify({
        "wishlist_id": wishlist_id,
        "wishlist_name": wishlist.name,
        "items": [{"id": item.id, "name": item.name, "image_url": item.image_url, "price": item.price} for item in items]
    }), 200

# ✅ Update Wishlist Name
@app.route("/wishlist/<int:wishlist_id>", methods=["PUT"])
def update_wishlist(wishlist_id):
    data = request.json
    wishlist = Wishlist.query.get(wishlist_id)

    if not wishlist:
        return jsonify({"message": "Wishlist not found"}), 404

    if data.get("name"):
        wishlist.name = data["name"]
        db.session.commit()

    return jsonify({"message": "Wishlist updated successfully!"}), 200

# ✅ Delete Wishlist
@app.route("/wishlist/<int:wishlist_id>", methods=["DELETE"])
def delete_wishlist(wishlist_id):
    wishlist = Wishlist.query.get(wishlist_id)
    if not wishlist:
        return jsonify({"message": "Wishlist not found"}), 404

    db.session.delete(wishlist)
    db.session.commit()

    return jsonify({"message": "Wishlist deleted successfully!"}), 200

# ✅ Update Individual Wishlist Item
@app.route('/wishlist/item/<int:item_id>', methods=['PUT'])
def update_wishlist_item(item_id):
    data = request.json
    item = Product.query.get(item_id)

    if not item:
        return jsonify({'message': 'Item not found'}), 404

    item.name = data.get('name', item.name)
    item.image_url = data.get('image_url', item.image_url)
    item.price = data.get('price', item.price)

    db.session.commit()
    return jsonify({'message': 'Item updated successfully!', 'item': {
        'id': item.id, 'name': item.name, 'image_url': item.image_url, 'price': item.price
    }}), 200

# ✅ Delete Individual Wishlist Item
@app.route('/wishlist/item/<int:item_id>', methods=['DELETE'])
def delete_wishlist_item(item_id):
    item = Product.query.get(item_id)

    if not item:
        return jsonify({'message': 'Item not found'}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully!'}), 200
@app.route("/products", methods=["GET"])
def get_all_products():
    items = Product.query.all()

    return jsonify({
        "products": [{"id": item.id, "name": item.name, "image_url": item.image_url, "price": item.price, "wishlist_id": item.wishlist_id} for item in items]
    }), 200
@app.route("/products", methods=["POST"])
def add_product():
    data = request.json

    # Validate input
    if not data.get("name") or not data.get("wishlist_id"):
        return jsonify({"message": "Product name and wishlist ID are required"}), 400

    # Create new product
    new_product = Product(
        name=data["name"], 
        image_url=data.get("image_url"), 
        price=data.get("price", 0),
        wishlist_id=data["wishlist_id"]
    )
    db.session.add(new_product)
    db.session.commit()

    return jsonify({
        "message": "Product added successfully!", 
        "product_id": new_product.id
    }), 201
