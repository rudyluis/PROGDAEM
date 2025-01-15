class Vehicle:

    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def __str__(self):
        return f'Color: {self.color}, Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}'
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

class Car(Vehicle):
    pass
    
    

bus = Bus("School Volvo", 180, 12)
car = Car("Audi Q5", 240, 18)
print(bus)
print(car)