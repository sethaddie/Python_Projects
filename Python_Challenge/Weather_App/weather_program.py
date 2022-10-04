from ast import Import
from pkgutil import ImpImporter
import requests
from pprint import pprint

API_Key ="b7a5147774fe90e4959635ab15b1f1e9"

city = input("Enter name of a city here:")


base_url = "http://api.openweathermap.org/data/2.5/weather?APPID="+API_Key+"&q="+city


weather_data= requests.get(base_url).json()

pprint(weather_data)