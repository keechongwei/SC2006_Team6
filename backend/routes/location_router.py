from flask import Blueprint, jsonify
from flask import request
from controllers import location_controller

location_bp = Blueprint('location', __name__, url_prefix='/api/location')

#get current gps location, only available on Windows
@location_bp.route('/get_current_location', methods=['GET'])
def get_Current_location():
    current_location = location_controller.getLoc()
    print(current_location)

    if current_location:
        location_data = {
            "latitude": current_location[0],
            "longitude": current_location[1]
        }
        return jsonify(location_data), 200
    else:
        return jsonify({"error": "Could not retrieve location data"}), 404
