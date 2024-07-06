from geopy import Nominatim
import sys

location_name = sys.argv[1]
geolocator = Nominatim(user_agent="ming")
location = geolocator.geocode("Sydney")

print(f"Latuitude: {location.latitude}")
print(f"Longitude: {location.longitude}")



