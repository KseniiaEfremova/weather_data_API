import requests


def get_lon_lat_of_location(location: str) -> tuple:
    """
    The function takes location, makes a get request and returns coordinates (lat, lon) from response.
    """
    api_key = "32261440bdece54cdcba512f82c431bc"
    url_location = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid={api_key}"
    response = requests.get(url_location)

    if response.status_code == 200:
        data = response.json()
        lat = data[0]["lat"]
        lon = data[0]["lon"]
    else:
        print(f"Error retrieving weather data: {response.text}")

    return lat, lon
