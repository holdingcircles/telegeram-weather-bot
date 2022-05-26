import requests
import datetime

from config import open_weather_key as api_key

# TODO make this a normal class, or
# 3 methods:
# get_coordinates - internal geocoding method
# get_current_weather - accepts a name, returns current weather
# get_forecast_weather - takes the name, returns the current forecast
# 

# class Weather:

#     def __init__(self) -> None:
#         pass

def get_coordinates(city='красноярск', api_key=api_key) -> tuple:
    """Retrun coordinates and name of the city"""
    try:
        # GET  request to geocoding API-function
        req = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}"
        )
        response = req.json()
        
        city_coordinates = []
        city_coordinates.append(response[0]['lat'])
        city_coordinates.append(response[0]['lon'])

    except Exception as ex:
        print(f'What came out?:\n {ex}')
    
    return tuple(city_coordinates)


def get_current_weather(city_lat, city_lon, api_key=api_key) -> str:
    """Return current weather by coordinates"""
    try:
        req = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?lat={city_lat}&lon={city_lon}&appid={api_key}&units=metric&lang=en'
        )

        response = req.json()

        city = response['name']
        temperature = response['main']['temp']
        feels_like = response['main']['feels_like']
        humidity = response['main']['humidity']
        pressure = response['main']['pressure']
        wind_speed = response['wind']['speed']
        sunrise_time = datetime.datetime.fromtimestamp(response['sys']['sunrise'])
        sunset_time = datetime.datetime.fromtimestamp(response['sys']['sunset'])

        return (f'\nПогода в городе {city}:\n'
             f'Temperature {int(temperature)} °C, feels like {int(feels_like)} °C.\n'
             f'Wind speed {"%.1f" % wind_speed} meters per second.\n'
             f'Humidity: {humidity}%.\nPressure: {pressure} mmHg.\n'
             f'Sunrise is at {datetime.datetime.time(sunrise_time)} and sunset is at {datetime.datetime.time(sunset_time)}.')

    except Exception as ex:
        return (f'Go see what came out?:\n\n {ex}')


# def get_forecast_weather(city_lat, city_lon, api_key=api_key):
#     try:
#         req = requests.get(
#             f'https://api.openweathermap.org/data/2.5/onecall?lat={city_lat}&lon={city_lon}&exclude=current,minutely,hourly,alerts&appid={api_key}&units=metric&lang=en'
#         )

#         response = req.json()

    # except Exception as ex:
    #     return(f'Come and see what's up?:\n\n {ex}')
