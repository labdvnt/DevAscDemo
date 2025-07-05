import yaml



with open('exampleRouter3.yaml') as file:
    data = yaml.safe_load(file)
print("**********" * 20)
print(data)  # YAML çıktısı
print("**********" * 20)
print(data["router"]["interfaces"][0])  # Tek tırnaklı YAML çıktısı
print("**********" * 20)