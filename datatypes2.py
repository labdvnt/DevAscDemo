from PythonClass.ClassTest import Car


my_car = Car(make="Toyota", model="Corolla", year=2020, mileage=15000, condition="New", color="Blue")
print(my_car.make)

print(my_car.__dict__)