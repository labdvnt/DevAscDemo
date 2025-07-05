import json

with open('exampleRouter2.json') as file:
    data = json.load(file)
print(data["router"]["interfaces"][0]) # Tek tırnaklı JSON çıktısı
print("**********" * 20)
json_data = json.dumps(data, indent=4)
print(json_data) # Çift tırnaklı python çıktısı