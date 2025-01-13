# Mars Nexus Wrapper

## Description

<table>
  <tr>
    <td style="vertical-align: top; padding-right: 20px;">
      The Mars Nexus Wrapper is a Python library that interfaces with multiple NASA APIs to fetch data related to Mars. The library provides functions for retrieving Mars weather data, orbital data, images from Mars rovers, and other Mars-related information.
    </td>
    <td>
      <img src="https://github.com/ericmaddox/mars-nexus-wrapper/blob/main/media/Mars_nexus_wrapper_logo2.PNG" width="1500"/>
    </td>
  </tr>
</table>

## Description

The **Mars Nexus Wrapper** is a Python library that interfaces with multiple NASA APIs to fetch data related to Mars. The library provides functions for retrieving Mars weather data, orbital data, images from Mars rovers, and other Mars-related information.

This wrapper is designed to interact with the following NASA endpoints:
- Mars rover photos
- Mars weather data (InSight)
- Mars orbital data (Astronomical data)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/mars-nexus-wrapper.git
    cd mars-nexus-wrapper
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the `.env` file with your NASA API key. Create a `.env` file in the root of the project and add:

    ```plaintext
    NASA_API_KEY=your_nasa_api_key
    ```

    You can obtain the API key from [NASA's official website](https://api.nasa.gov/).

## Usage

Once you have installed the package and set up your API key, you can use the wrapper to fetch Mars-related data. Below is an example of how to use the functions from the wrapper:

```python
from Mars_Wrapper.weather import get_latest_weather
from Mars_Wrapper.orbital import get_orbital_data
from Mars_Wrapper.imaging import get_latest_images

# Fetch latest Mars weather data
weather = get_latest_weather()
print(weather)

# Fetch Mars orbital data
orbital_data = get_orbital_data()
print(orbital_data)

# Fetch latest Mars rover images
images = get_latest_images(sol=1000, camera="FHAZ")
print(images)
```

## Folder Structure

```
mars-nexus-wrapper/
│
├── .env                  # Contains environment variables (e.g., API keys)
├── Mars_Wrapper/         # Contains the main wrapper code
│   ├── imaging.py        # Handles Mars rover images
│   ├── orbital.py        # Handles Mars orbital data
│   ├── utils.py          # Utility functions and API response handling
│   ├── weather.py        # Handles Mars weather data
│
├── Tests/                # Contains unit tests
│   ├── tests_utils.py    # Tests for utils.py
│   ├── tests_weather.py  # Tests for weather.py
│   ├── tests_imaging.py  # Tests for imaging.py
│   ├── tests_orbital.py  # Tests for orbital.py
│
├── main.py               # Example entry point for fetching Mars data
├── requirements.txt      # List of dependencies
└── README.md             # This file
```

## Tests

This project uses `pytest` for testing.

To run the tests:

1. Install test dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the tests using `pytest`:

    ```bash
    pytest
    ```

### Test Files

- **tests_utils.py**: Tests for utility functions (`handle_api_response`)
- **tests_weather.py**: Tests for weather data functions
- **tests_imaging.py**: Tests for Mars rover imaging functions
- **tests_orbital.py**: Tests for Mars orbital data functions

## Acknowledgments

- [NASA](https://api.nasa.gov/) for providing public APIs for Mars-related data.
