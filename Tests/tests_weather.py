import sys
import os

# Add the parent directory of the current file to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Mars_Wrapper.weather import get_latest_weather  # Ensure this is correctly imported

def test_get_latest_weather():
    result = get_latest_weather()
    assert result is not None  # Replace this with a meaningful test
