# services/user-service/app.py
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# In-memory storage (in production, use a database)
users = {}

@app.route('/health')
def health():
    return jsonify({'status': 'User service is healthy'}), 200

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = str(uuid.uuid4())
    user = {
        'id': user_id,
        'name': data.get('name'),
        'email': data.get('email')
    }
    users[user_id] = user
    return jsonify(user), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)