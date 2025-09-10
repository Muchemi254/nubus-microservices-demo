# services/gateway-service/routes.py
from flask import Blueprint, jsonify, request
import requests
import os

api = Blueprint('api', __name__)

USER_SERVICE_URL = os.getenv('USER_SERVICE_URL', 'http://localhost:5001')
PRODUCT_SERVICE_URL = os.getenv('PRODUCT_SERVICE_URL', 'http://localhost:5002')

@api.route('/')
def index():
    return jsonify({
        'message': 'Nubus Microservices Gateway',
        'endpoints': {
            'users': '/api/users',
            'products': '/api/products'
        }
    })

# User service routes
@api.route('/api/users', methods=['GET'])
def get_users():
    response = requests.get(f'{USER_SERVICE_URL}/users')
    return jsonify(response.json()), response.status_code

@api.route('/api/users', methods=['POST'])
def create_user():
    response = requests.post(f'{USER_SERVICE_URL}/users', json=request.json)
    return jsonify(response.json()), response.status_code

@api.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    response = requests.get(f'{USER_SERVICE_URL}/users/{user_id}')
    return jsonify(response.json()), response.status_code

# Product service routes
@api.route('/api/products', methods=['GET'])
def get_products():
    response = requests.get(f'{PRODUCT_SERVICE_URL}/products')
    return jsonify(response.json()), response.status_code

@api.route('/api/products', methods=['POST'])
def create_product():
    response = requests.post(f'{PRODUCT_SERVICE_URL}/products', json=request.json)
    return jsonify(response.json()), response.status_code

@api.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    response = requests.get(f'{PRODUCT_SERVICE_URL}/products/{product_id}')
    return jsonify(response.json()), response.status_code