import requests
import json

url = "https://swapi.info/api/people/"

payload = {}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()

for person in data:
    if person['name'] == 'Leia Organa':
        print(json.dumps(person, indent=4))