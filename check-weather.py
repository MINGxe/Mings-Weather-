import openmeteo_requests

from datetime import date

import requests
import urllib
import sys



def get_the_weather_data():
    openmeteo = openmeteo_requests.Client()

    location_name = sys.argv[1]

    print (location_name)

    url = "http://api.open-meteo.com/v1/forecast"

    location = print_my_location(location_name)

    params = {
        "latitude":location['latitude'],
        "longitude":location['longitude'],
        "daily": ["temperature_2m_max", "temperature_2m_min"]
    }

    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]

    daily = response.Daily()
    daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
    daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
    return {"tempretures_high":daily_temperature_2m_max[0],
    "tempretures_low":daily_temperature_2m_min[0],
    "Date":date.today(),
    "Location":location_name}

def print_the_weather(weather_data):
    print(weather_data['Date'])
    print(weather_data['Location'])
    print(f"Tempretures_high:{weather_data['tempretures_high']} Celsus")
    print(f"Tempretures_low: {weather_data['tempretures_low']} Celsus")






def print_my_location(location_name):
    url = 'https://geocoding-api.open-meteo.com/v1/search'
    params = {
    'name': location_name,
    'limit': 1
    }
    response = requests.get(f'{url}?{urllib.parse.urlencode(params)}')
    json_data = response.json()
    print (json_data)
    
    return {'latitude': json_data['results'][0]['latitude'],
    'longitude': json_data['results'][0]['longitude']}

    









weather_data=get_the_weather_data()
print_the_weather(weather_data)


   