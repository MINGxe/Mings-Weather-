import openmeteo_requests

from datetime import date, datetime

import requests
import urllib
import sys



def get_the_weather_data():
    openmeteo = openmeteo_requests.Client()

    location_name = sys.argv[1]

    url = "http://api.open-meteo.com/v1/forecast"

    location = print_my_location(location_name)

    input_date_text = sys.argv[2]
    target_date = datetime.strptime(input_date_text, '%d/%m/%Y')


    MAX_DAYS_FROM_TODAY = 16
    days_from_today = (target_date.date() - date.today()).days

    if ((days_from_today > MAX_DAYS_FROM_TODAY) or (days_from_today < 0)):
       print(f'Data not available for {target_date.date()}')
       exit(code=1)

    params = {
        "latitude":location['latitude'],
        "longitude":location['longitude'],
        "daily": ["temperature_2m_max", "temperature_2m_min"],
        "forecast_days": MAX_DAYS_FROM_TODAY
    }

    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]

    daily = response.Daily()
    daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
    daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
    return {"tempretures_high":daily_temperature_2m_max[days_from_today],
    "tempretures_low":daily_temperature_2m_min[days_from_today],
    "Date":target_date.date(),
    "Location":location_name}

def print_the_weather(weather_data):
    print(weather_data['Date'])
    print(weather_data['Location'])
    print(f"Tempretures_high:{weather_data['tempretures_high']} Celsus")
    print(f"Tempretures_low: {weather_data['tempretures_low']} Celsus")


def print_my_date():
    # Input examples:
    # 20/07/2024
    print('')


def print_my_location(location_name):
    url = 'https://geocoding-api.open-meteo.com/v1/search'
    params = {
    'name': location_name,
    'limit': 1
    }
    response = requests.get(f'{url}?{urllib.parse.urlencode(params)}')
    json_data = response.json()

    return {'latitude': json_data['results'][0]['latitude'],
    'longitude': json_data['results'][0]['longitude']}











weather_data=get_the_weather_data()
print_the_weather(weather_data)



   