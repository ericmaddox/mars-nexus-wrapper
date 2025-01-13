from Mars_Wrapper.weather import get_latest_weather
from Mars_Wrapper.orbital import get_orbital_data  # Corrected function name
from Mars_Wrapper.imaging import get_latest_images

def main():
    print("Fetching latest Mars weather...")
    print(get_latest_weather())

    print("\nFetching Mars orbital data...")  # Adjusted description
    print(get_orbital_data())  # Corrected function name

    print("\nFetching latest Mars rover images...")
    print(get_latest_images())

if __name__ == "__main__":
    main()
