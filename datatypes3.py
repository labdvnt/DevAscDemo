# File: datatypes3.py
from PythonClass.challangeClassFunction import Person

# Create an instance of the Person class
person = Person("Omer", "Dartar", 25, 180)

print(person.__dict__)

print(f"Person's name: {person.first_name} {person.last_name}")
print(f"Person's age: {person.age}")
print(f"Person's height: {person.height_cm} cm")