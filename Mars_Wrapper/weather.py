import requests
from Mars_Wrapper.utils import NASA_API_KEY, handle_api_response

BASE_URL = "https://api.nasa.gov/insight_weather/"

def get_latest_weather():
    """Fetch the latest weather data from Mars."""
    params = {"api_key": NASA_API_KEY, "feedtype": "json", "ver": "1.0"}
    response = requests.get(BASE_URL, params=params)
    return handle_api_response(response)
