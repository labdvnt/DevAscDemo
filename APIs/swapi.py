
import requests


base_url = "https://swapi.info/api/"
endpoints = "people/"

response = requests.get(f"{base_url}{endpoints}")
data = response.json()
print(data)
print(data[0])










