import json

def print_the_weather(weather_data):
    print(weather_data['Date'])
    print(weather_data['Location'])
    print(f"Tempretures_high:{weather_data['tempretures_high']} Celsus")
    print(f"Tempretures_low: {weather_data['tempretures_low']} Celsus")

def read_history_file():
    history_filepath = 'check-weather-history.ndjson'
    with open(file=history_filepath, mode='r') as file:
        for line in file:
            json_data = json.loads(line)
            print_the_weather(json_data)

read_history_file()
