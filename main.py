import requests

api_key = "secret_key"


class WeatherAPIException(Exception):
    """Raised when the response has an error status code"""

    def __init__(self, message):
        self.message = message


def get_lon_lat_of_location(location: str):
    """
    The function takes location, makes a get-request
    and returns coordinates (latitude,longitude) from response
    or raise WeatherAPIException, if the request was not successful.

    Return:
        tuple: lat and lon - if the request was successful
        or
        raise WeatherAPIException: if the request was not successful
    """

    url_location = f"http://api.openweathermap.org/geo/1.0/direct?q" \
                   f"={location}&limit=1&appid={api_key}"

    response = requests.get(url_location)

    if response.status_code != 200:
        raise WeatherAPIException(
            f"Geo API replied with code {response.status_code}")

    data = response.json()
    lat = data[0]["lat"]
    lon = data[0]["lon"]
    return lat, lon


def get_weather_data(lat: str, lon: str):
    """
    The function takes latitude and longitude of location, makes get-request
    and returns weather data in json format
    or raise WeatherAPIException, if the request was not successful.

    Return:
        response.json(): if the request was successful
        or
        raise WeatherAPIException: if there is error status code
    """

    url = f"https://api.openweathermap.org/data/2.5/weather?" \
          f"lat={lat}&lon={lon}&exclude=hourly,daily&appid={api_key}"

    response = requests.get(url)
    if response.status_code != 200:
        raise WeatherAPIException(
            f"Weather API replied with code {response.status_code}")
    return response.json()


def main():
    """
    The function asks user to input location,
    and displays weather of this location to user.
    """

    location = input("Enter a location (e.g. 'New York, NY'): ")
    try:
        lat, lon = get_lon_lat_of_location(location)
        weather_data = get_weather_data(lat, lon)
    except Exception as e:
        print("Error during weather API call:", e)
        return
    if weather_data and lat and lon:
        temperature = round(int(weather_data["main"]["temp"]) - 273.15, 2)
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        print(
            f"The temperature in {location} is {temperature}°C, "
            f"the humidity is {humidity}%, "
            f"and the weather is {description}.")
    else:
        print(f"Error retrieving weather data")


if __name__ == "__main__":
    main()
