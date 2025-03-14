from flask import Blueprint, jsonify
from flask_pymongo import PyMongo
from flask import request
from models.user import User, AccountState


user_bp = Blueprint('user', __name__, url_prefix='/api/users')
mongo = None

def init_mongo(mongo_instance):
    global mongo
    mongo = mongo_instance

@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    
    user = User(
        user_id=None,
        name=data.get('name'),
        email=data.get('email'),
        password=data.get('password'),  
        age=data.get('age', 0),
        is_student=data.get('is_student', True)
    )
    
    # Pass the mongo instance to the save method
    user_id = user.save(mongo)
    
    return jsonify({"success": True, "user_id": user_id})