# services/product-service/app.py
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# In-memory storage (in production, use a database)
products = {}

@app.route('/health')
def health():
    return jsonify({'status': 'Product service is healthy'}), 200

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(list(products.values())), 200

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product), 200
    return jsonify({'error': 'Product not found'}), 404

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product_id = str(uuid.uuid4())
    product = {
        'id': product_id,
        'name': data.get('name'),
        'price': data.get('price')
    }
    products[product_id] = product
    return jsonify(product), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)