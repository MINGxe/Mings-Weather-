# Ming's weather CLI

present real time tempreture from a weather API

Feature 1: Search tempreture by location by city

Feature 2: Search tempreture today or future date 

Feature 3 :Display history search results 

## Github Repository
https://github.com/MINGxe/Mings-Weather-/tree/main

## Requirements

VS code

python3

pip3

## Installation

Unzip the zip file

open the folder with vs code

Install python packages with terminal using requirements txt file in this repository.
```
pip3 install -r requirements.txt

```

## Usage

Check tempreture using this command:

```
python3 check-weather.py
```

Check today`s tempreture with location(any city name) with this command:

```
python3 check-weather.py sydney
```

Check today`s tempreture with location and a given date (16 days after current day) with this command (Date format must in dd/mm/yyyy):
```
python3 check-weather.py sydney 10/7/2024
```

Check the history using this command:

```
python3 check-history.py
```
