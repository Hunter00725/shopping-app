from flask import Flask, jsonify

app = Flask(__name__)

# Sample Product Database
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 999},
    {"id": 2, "name": "Smartphone", "price": 499},
    {"id": 3, "name": "Headphones", "price": 149}
]

@app.route('/')
def home():
    return "<h1>Welcome to the Shopping App (v1)</h1><p>Navigate to /products to view items.</p>"

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"status": "success", "products": PRODUCTS})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
