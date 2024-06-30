import openmeteo_requests

from datetime import date



def get_the_weather_data():
    openmeteo = openmeteo_requests.Client()

    url = "http://api.open-meteo.com/v1/forecast"

    params = {
        "latitude":52.52,
        "longitude": 13.41,
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
    "Location":"Sydney"}

def print_the_weather(weather_data):
    print(weather_data['Date'])
    print(weather_data['Location'])
    print(f"Tempretures_high:{weather_data['tempretures_high']} Celsus")
    print(f"Tempretures_low: {weather_data['tempretures_low']} Celsus")

weather_data=get_the_weather_data()
print_the_weather(weather_data)


   