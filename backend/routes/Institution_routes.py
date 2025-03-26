from flask import Blueprint, jsonify, request
from models.Institutions import Institution, InstitutionType
from bson.objectid import ObjectId
from bson.errors import InvalidId

institution_bp = Blueprint('institution', __name__, url_prefix='/api/institutions')
mongo = None

def init_mongo(mongo_instance):
    global mongo
    mongo = mongo_instance

@institution_bp.route('/getall', methods=['GET'])
def get_all_institutions():
    
    try:
        institutions = Institution.find_all(mongo)
        return jsonify({
            "success": True,
            "message": "Institutions retrieved successfully",
            "data": institutions
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error retrieving institutions: {str(e)}",
            "data": None
        }), 500