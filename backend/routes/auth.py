from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
import database as db

bcrypt = Bcrypt()
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_pw = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    
    user = {
        "username": data['username'],
        "password": hashed_pw,
        "email": data['email'],
    }
    
    if db.users_collection.find_one({"username": data["username"]}):
        return jsonify({"message": "User already exists"}), 400

    db.users_collection.insert_one(user)
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = db.users_collection.find_one({"username": data["username"]})
    
    if user and bcrypt.check_password_hash(user['password'], data['password']):
        access_token = create_access_token(identity=data["username"])
        return jsonify({"message": "Login successful", "token": access_token}), 200
    return jsonify({"message": "Invalid credentials"}), 401
