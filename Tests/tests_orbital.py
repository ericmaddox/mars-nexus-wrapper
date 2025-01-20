import sys
import os

# Add the Mars_Wrapper directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Mars_Wrapper')))

# Import the function to test
from Mars_Wrapper.orbital import get_orbital_data

def test_get_orbital_data():
    result = get_orbital_data()
    assert result is not None  # Replace with appropriate test conditions
