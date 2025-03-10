import requests
import pymongo
import atexit

def fetch_hawker_data():
    """
    Fetches hawker centre data from the API.
    """
    dataset_id = "d_4a086da0a5553be1d89383cd90d07ecd"
    url = f"https://api-open.data.gov.sg/v1/public/api/datasets/{dataset_id}/poll-download"

    try:
        response = requests.get(url)
        json_data = response.json()

        if json_data['code'] != 0:
            print(f"Error: {json_data['errMsg']}")
            return None

        # Fetch the actual data file URL
        data_url = json_data['data']['url']
        response = requests.get(data_url)

        return response.json()  # Assuming the response is in JSON format

    except requests.exceptions.RequestException as e:
        print(f"API Request Failed: {e}")
        return None
