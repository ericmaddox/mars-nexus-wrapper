import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Retrieve the API key
NASA_API_KEY = os.getenv("NASA_API_KEY")

def handle_api_response(response):
    """Handle API response and return data or raise an error."""
    if response.status_code == 200:
        return response.json()
    else:
        # Raise an exception if the status code is not 200
        raise Exception(f"API request failed with status code {response.status_code}")
