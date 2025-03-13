from flask import Blueprint, jsonify
from database import get_hawker_collection
hawker_bp = Blueprint("hawker", __name__)


@hawker_bp.route("/hawker-centres", methods=["GET"])
def get_hawker_centres():
    hawker_collection = get_hawker_collection()  # Get the initialized collection

    if hawker_collection is None:
        return jsonify({"error": "MongoDB collection not initialized"}), 500

    try:
        data = list(hawker_collection.find({}, {"_id": 0}))  # Exclude `_id`
        print(data)  # Debugging

        if not data:
            return jsonify({"message": "No hawker centres found"}), 200

        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
