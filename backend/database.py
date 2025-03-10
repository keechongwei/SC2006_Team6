import pymongo
from flask import jsonify
from bs4 import BeautifulSoup
import requests
hawker_collection = None
user_collection = None

def parse_html_table(html_content):
    """
    Parses an HTML table and extracts key-value pairs.
    """
    parsed_data = {}

    # Check if description is valid HTML
    if not html_content or "<table" not in html_content:
        return parsed_data

    soup = BeautifulSoup(html_content, "html.parser")
    table_rows = soup.find_all("tr")  # Find all table rows

    for row in table_rows:
        cells = row.find_all("th") + row.find_all("td")  # Get all headers and data
        if len(cells) == 2:  # Ensure we have key-value pairs
            key = cells[0].get_text(strip=True)
            value = cells[1].get_text(strip=True)
            parsed_data[key] = value

    return parsed_data


def fetch_hawker_data():
    """
    Fetches and formats hawker centre data from the API.
    """
    dataset_id = "d_4a086da0a5553be1d89383cd90d07ecd"
    url = f"https://api-open.data.gov.sg/v1/public/api/datasets/{dataset_id}/poll-download"

    try:
        response = requests.get(url)
        json_data = response.json()

        if json_data['code'] != 0:
            print(f"Error: {json_data['errMsg']}")
            return []

        # Fetch the actual data file URL
        data_url = json_data['data']['url']
        response = requests.get(data_url)
        raw_data = response.json()  # JSON response with 'features' key

        # Debugging: Print one sample feature to check structure

        formatted_data = []
        for feature in raw_data.get("features", []):
            properties = feature.get("properties", {})
            geometry = feature.get("geometry", {})

            # Extract values normally
            name = properties.get("Name", "Unknown")
            description = properties.get("Description", "")

            # Extract key-value pairs from HTML inside `Description`
            extracted_properties = parse_html_table(description)

            # Combine extracted values with existing properties
            hawker_centre = {
                "name": extracted_properties.get("NAME", name),  
                "description": extracted_properties.get("DESCRIPTION", "No description available"),
                "address": {
                    "block": extracted_properties.get("ADDRESSBLOCKHOUSENUMBER", "Unknown"),
                    "street": extracted_properties.get("ADDRESSSTREETNAME", "Unknown"),
                    "building": extracted_properties.get("ADDRESSBUILDINGNAME", "Unknown"),
                    "postal_code": extracted_properties.get("ADDRESSPOSTALCODE", "Unknown"),
                },
                "status": extracted_properties.get("STATUS", "Unknown"),
                "photo_url": extracted_properties.get("PHOTOURL", ""),
                "co_locators": extracted_properties.get("INFO_ON_CO_LOCATORS", ""),
                "location": {
                    "latitude": geometry.get("coordinates", [None, None])[1],
                    "longitude": geometry.get("coordinates", [None, None])[0],
                }
            }

            formatted_data.append(hawker_centre)

        return formatted_data

    except requests.exceptions.RequestException as e:
        print(f"API Request Failed: {e}")
        return []


def get_hawker_collection():
    """ Returns the initialized MongoDB collection for hawker centres. """
    return hawker_collection

def get_user_collection():
    """ Returns the initialized MongoDB collection for hawker centres. """
    return user_collection

def init_db(mongo_uri):
    """
    Initializes MongoDB connection.
    """
    global hawker_collection,user_collection

    client = pymongo.MongoClient(mongo_uri)
    db = client["hawker_app_db"]
    write_data(fetch_hawker_data(),db['hawker_centres'])
    hawker_collection = db["hawker_centres"]
    user_collection = db["users"]
    return db


def write_data(data, collection):
    """
    Writes data to the specified MongoDB collection.
    """
    if data:
        try:
            # Clear existing data to prevent duplicates
            delete_result = collection.delete_many({})
            print(f"Deleted {delete_result.deleted_count} old records in {collection.name}.")

            # Insert new data
            insert_result = collection.insert_many(data)
            print(f"Inserted {len(insert_result.inserted_ids)} new records into {collection.name}.")

        except Exception as e:
            print(f"Error writing to MongoDB: {e}")
    else:
        print(f"No data to write to {collection.name}.")
