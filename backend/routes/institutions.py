from flask import Blueprint, request, jsonify
import db

institutions_bp = Blueprint('institutions', __name__)

@institutions_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    results = list(db.institutions_collection.find({"name": {"$regex": query, "$options": "i"}}, {"_id": 0}))
    
    if not results:
        return jsonify({"message": "No institutions found"}), 404

    return jsonify(results), 200
