import sys
import os

# Add the parent directory of 'Mars_Wrapper' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Mars_Wrapper')))

from Mars_Wrapper.imaging import get_latest_images

def test_get_latest_images():
    # Test with default sol and camera parameters
    result = get_latest_images()
    assert result is not None  # Check if the result is not None, indicating a successful API call
    assert isinstance(result, dict)  # Assuming the response is a dictionary
    # Additional assertions can be added depending on the structure of the response
