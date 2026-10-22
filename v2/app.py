from flask import Flask, jsonify, request

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 999},
    {"id": 2, "name": "Smartphone", "price": 499},
    {"id": 3, "name": "Headphones", "price": 149}
]

# In-memory Cart storage
cart = []

@app.route('/')
def home():
    return "<h1>Welcome to the Shopping App (v2)</h1><p>/products (GET) | /cart (GET, POST)</p>"

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products": PRODUCTS})

@app.route('/cart', methods=['GET'])
def get_cart():
    return jsonify({"cart": cart})

@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if product:
        cart.append(product)
        return jsonify({"message": f"{product['name']} added to cart", "cart": cart}), 201
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
