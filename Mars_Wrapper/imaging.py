# Mars_Wrapper/imaging.py

import requests
from Mars_Wrapper.utils import NASA_API_KEY, handle_api_response

BASE_URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

def get_latest_images(sol=1000, camera="FHAZ"):
    """Fetch latest Mars rover images."""
    params = {"sol": sol, "camera": camera, "api_key": NASA_API_KEY}
    response = requests.get(BASE_URL, params=params)
    return handle_api_response(response)
