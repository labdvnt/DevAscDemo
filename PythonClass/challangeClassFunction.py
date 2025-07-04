class Person:
    def __init__(self, first_name, last_name, age, height_cm):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height_cm = height_cm
        self.is_happy = True  # default property

    def greet(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}.")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! I am now {self.age} years old.")

    def jump(self):
        print(f"{self.first_name} jumps up in the air!")

# Example usage:
# person = Person("Omer", "Dartar", 25, 180)
# person.greet()
# person.celebrate_birthday()
# person.jump()