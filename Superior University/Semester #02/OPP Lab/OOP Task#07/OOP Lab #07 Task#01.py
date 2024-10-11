# Vehical Rental System

class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def display_info(self):
        print(f"Make :{self.make} Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model,num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors
    def display_info(self):
        print(f"Make: {self.make} Model: {self.model} No of Doors: {self.num_doors}")

class LuxuryCar(Car):
    def __init__(self, make, model, num_doors, features):
        super().__init__(make, model, num_doors)
        self.features = features
    def additional_info(self):
        print(f"Make: {self.make} Model: {self.model} No of Doors: {self.num_doors} Features: {self.features}")

vehicle = Vehicle("Mustang", 1964)
vehicle.display_info()
car = Car("Koenigsegg", 2022, 2)
car.display_info()
luxury = LuxuryCar("Rolls Royce Ghost", 2019, 4, "Selling Stars")
luxury.additional_info()