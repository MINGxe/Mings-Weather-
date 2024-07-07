import openmeteo_requests
import json

from datetime import date, datetime

import requests
import urllib
import sys



def get_the_weather_data():
    openmeteo = openmeteo_requests.Client()
    if len(sys.argv) > 1:
        location_name = sys.argv[1]
    else:
        location_name = get_user_input_location()

    url = "http://api.open-meteo.com/v1/forecast"

    location = print_my_location(location_name)

    if len(sys.argv) > 2:
        input_date_text = sys.argv[2]
        try:
            target_date = datetime.strptime(input_date_text, '%d/%m/%Y').date()
        except ValueError as error:
            print("Incorrect date format, please use dd/mm/yy")
            exit(1)
    else:
        target_date = date.today()

    MAX_DAYS_FROM_TODAY = 16
    days_from_today = (target_date - date.today()).days

    if ((days_from_today > MAX_DAYS_FROM_TODAY) or (days_from_today < 0)):
       print(f'Data not available for {target_date}')
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
    return {"tempretures_high":round(float(daily_temperature_2m_max[days_from_today]), 2),
    "tempretures_low":round(float(daily_temperature_2m_min[days_from_today]), 2),
    "Date":target_date,
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

    if 'results' not in json_data or len(json_data['results']) == 0: 
        print("Incorrect location name.")
        exit(1)


    return {'latitude': json_data['results'][0]['latitude'],
    'longitude': json_data['results'][0]['longitude']}


def get_user_input_location():
    while True:
        user_input = input('Enter a location(or press Enter to exit):')
        if user_input is not "":
            return user_input
        else:
            exit()

def save_the_weather(weather_data):
    history_filepath = 'check-weather-history.ndjson'

    json_weather_data = {
        "tempretures_high":weather_data['tempretures_high'],
        "tempretures_low":weather_data['tempretures_low'],
        "Date":str(weather_data['Date']),
        "Location":weather_data['Location']
    }
    with open(file=history_filepath, mode='a') as file:
        file.write(json.dumps(json_weather_data) + '\n')


weather_data=get_the_weather_data()
save_the_weather(weather_data)
print_the_weather(weather_data)


