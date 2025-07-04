class Car:
    def __init__(self, make: str, model: str, year: int, mileage: int, condition: str, color: str) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.condition = condition
        self.color = color
        self.running = False
        self.speed = 0
    
    def start(self) -> None:
        if self.running:
            print(f"The {self.make} {self.model} is already running.")
        else:
            self.running = True
            print(f"The {self.make} {self.model} has started.")

    def stop(self) -> None:
        if not self.running:
            print(f"The {self.make} {self.model} is already stopped.")
        else:
            self.running = False
            print(f"The {self.make} {self.model} has stopped.")

    def accelerate(self, increment: int) -> None:
        if not self.running:
            print(f"Cannot accelerate. The {self.make} {self.model} is not running.")
        else:
            self.speed += increment
            print(f"The {self.make} {self.model} is now going {self.speed} mph.")
    

