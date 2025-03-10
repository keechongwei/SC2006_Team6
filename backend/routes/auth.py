from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from database import get_user_collection

bcrypt = Bcrypt()
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_pw = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user_collection = get_user_collection()

    user = {
        "username": data['username'],
        "password": hashed_pw,
        "email": data['email'],
    }
    
    if user_collection.find_one({"username": data["username"]}):
        return jsonify({"message": "User already exists"}), 400

    user_collection.insert_one(user)
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_collection = get_user_collection()
    user = user_collection.find_one({"username": data["username"]})
    
    if user and bcrypt.check_password_hash(user['password'], data['password']):
        access_token = create_access_token(identity=data["username"])
        return jsonify({"message": "Login successful", "token": access_token}), 200
    return jsonify({"message": "Invalid credentials"}), 401
