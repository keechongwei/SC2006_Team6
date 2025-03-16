from flask import Blueprint, jsonify,request
from database import get_hawker_data
from math import radians, sin, cos, sqrt, atan2

hawker_summary = {}
hawker_bp = Blueprint("hawker", __name__)

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance in kilometers between two points
    given their latitude and longitude using the Haversine formula.
    """
    R = 6371  # Radius of Earth in km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c  # Distance in km

@hawker_bp.route("/hawker-centres", methods=["GET"])
def get_hawker_centres():
    global hawker_summary 
    hawker_summary = get_hawker_data()  # Get the initialized collection

    if hawker_summary is None:
        return jsonify({"error": "MongoDB collection not initialized"}), 500

@hawker_bp.route("/find-nearby-hawkers", methods=["GET"])
def find_nearby_hawkers():
    """
    Finds hawker centres within a given radius (default 1 km) of the input latitude and longitude.
    Returns a list of nearby hawker centres with name, latitude, and longitude.
    """
    get_hawker_centres()
    
    try:
        # Extract query parameters
        lat = request.args.get('latitude', type=float)
        lon = request.args.get('longitude', type=float)

        # Ensure values are provided
        if lat is None or lon is None:
            return jsonify({"error": "Missing latitude or longitude parameters"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    nearby_centres = []
    radius = 1  # 1 km radius

    for name, details in hawker_summary.items():
        hawker_lat = details["location"].get("latitude")
        hawker_lon = details["location"].get("longitude")
        
        if hawker_lat is None or hawker_lon is None:
            continue  # Skip if coordinates are missing

        distance = haversine(lat, lon, hawker_lat, hawker_lon)

        if distance <= radius:
            nearby_centres.append({
                "name": name,
                "latitude": hawker_lat,
                "longitude": hawker_lon,
                "distance_km": round(distance, 2)
            })

    return jsonify({"nearby_centres": nearby_centres})
