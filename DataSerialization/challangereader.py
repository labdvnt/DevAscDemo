import yaml

with open('challangeJson.json') as file:
    data = yaml.safe_load(file)
print("**********" * 20)
print(data)  # YAML çıktısı
print("**********" * 20)
print(data["arabalar"]["araba"][0])
print("**********" * 20)
print(data["arabalar"]["araba"][0]["marka"])
print("**********" * 20)