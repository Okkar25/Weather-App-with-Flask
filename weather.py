from dotenv import load_dotenv
from pprint import pprint
import requests
import os
import json

load_dotenv()

api_key = os.getenv("API_KEY")


def get_current_weather(city="Yangon"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(request_url)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(
            f"Error: Unable to get weather data for {city}. HTTP Status code: {response.status_code}"
        )
        return None


if __name__ == "__main__":
    print("\n*************** Get Current Weather Conditions ***************\n")

    city = input("\nPlease enter a city : ")

    weather_data = get_current_weather(city)

    if weather_data is not None:
        # print()
        # pprint(weather_data)
        # print()

        print()
        print(json.dumps(weather_data, indent=4, sort_keys=True))
        print()
    else:
        print(
            f"Could not retrieve weather for {city}. Please check the city name and try again."
        )
