from flask import Blueprint, jsonify
from flask_pymongo import PyMongo

test_mongo_bp = Blueprint('test_mongo', __name__)

# Store the PyMongo instance that will be set from the main app
mongo = None

def init_mongo(mongo_instance):
    global mongo
    mongo = mongo_instance

@test_mongo_bp.route('/test_connection', methods=['GET'])
def test_connection():
    try:
        # Get the client from PyMongo
        client = mongo.cx
        
        # Try to get server info
        server_info = client.server_info()
        
        # Try a simple database operation
        db_list = client.list_database_names()
        
        return jsonify({
            "success": True,
            "message": "Successfully connected to MongoDB Atlas!",
            "server_info": str(server_info),
            "databases": db_list
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Failed to connect to MongoDB Atlas: {str(e)}"
        })