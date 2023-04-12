import requests
from utils import get_lon_lat_of_location


def get_weather_data():
    """
    The function asks user to input  location, makes get-request, gets weather data and display to user
    """
    api_key = "32261440bdece54cdcba512f82c431bc"
    location = input("Enter a location (e.g. 'New York, NY'): ")
    lat, lon = get_lon_lat_of_location(location)

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&exclude=hourly,daily&appid={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()

        temperature = round(int(weather_data["main"]["temp"])-273.15, 2)
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        print(
            f"The temperature in {location} is {temperature}°C, the humidity is {humidity}%, "
            f"and the weather is {description}.")
    else:
        print(f"Error retrieving weather data: {response.text}")


if __name__ == "__main__":
    get_weather_data()