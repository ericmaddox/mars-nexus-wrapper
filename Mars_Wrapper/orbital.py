import requests
from Mars_Wrapper.utils import handle_api_response, NASA_API_KEY

# API endpoint for Mars mission data (adjust accordingly if a specific API is available)
MARS_ORBITAL_API_URL = "https://api.nasa.gov/planetary/mars/"

def get_mars_orbital_data(date=None):
    """
    Fetch Mars orbital data from NASA's Mars mission.
    :param date: Optional, fetch data for a specific date (YYYY-MM-DD).
    :return: Parsed API response.
    """
    params = {"api_key": NASA_API_KEY}
    if date:
        params["date"] = date
    response = requests.get(MARS_ORBITAL_API_URL, params=params)
    return handle_api_response(response)