from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from database import get_user_collection
from models.user import User

bcrypt = Bcrypt()
login_bp = Blueprint('auth', __name__)

def init_mongo(mongo_instance):
    global mongo
    mongo = mongo_instance

@login_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_pw = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user_collection = get_user_collection()

    user = User(
        user_id=None,
        username=data.get('username'),
        email=data.get('email'),
        password=hashed_pw,  
        age=data.get('age', 0),
        is_student=data.get('is_student', True)
    )
    if user_collection.find_one({"username": data["username"]}):
        return jsonify({"message": "User already exists"}), 400
    # Pass the mongo instance to the save method
    else:
        user.save(mongo)
        return jsonify({"message": "User registered successfully"}), 201

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_collection = get_user_collection()
    user = user_collection.find_one({"username": data["username"]})
    
    if not user:
        return jsonify({"message": "User does not exist"}), 401  # ✅ Ensure proper response

    stored_password_hash = user["password"]
    entered_password = data["password"]

    # ✅ Correct: Check the entered password against the stored hash
    if bcrypt.check_password_hash(stored_password_hash, entered_password):  
        access_token = create_access_token(identity=data["username"])
        return jsonify({"message": "Login successful", "token": access_token}), 200

    return jsonify({"message": "Invalid credentials"}), 401