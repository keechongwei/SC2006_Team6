import asyncio
from geopy.geocoders import Nominatim
import requests


async def get_coords():
    geolocator = Nominatim(user_agent="geoapiExercises")

    try:
        # Get location based on IP if precise GPS is unavailable
        response = requests.get("https://ipinfo.io/json")
        data = response.json()

        if "loc" in data:
            latitude, longitude = map(float, data["loc"].split(","))
            return [latitude, longitude]
        else:
            # Fallback method (geocode city)
            location = geolocator.geocode("Your City")
            if location:
                return [location.latitude, location.longitude]

        return None

    except Exception as e:
        print(f"Error retrieving location: {e}")
        return None


def get_loc():
    try:
        return asyncio.run(get_coords())
    except PermissionError:
        print("ERROR: You need to allow applications to access your location settings")


print(get_loc())
