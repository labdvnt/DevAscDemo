import xmltodict

with open('exampleRouter.xml') as file:
    xml_data = file.read()
data_dict = xmltodict.parse(xml_data)
print(data_dict)
print("************" * 20) 
data = data_dict["router"]["interfaces"]["interface"][0]['name']
print(data)