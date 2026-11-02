class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")
my_car = car("Toyota", "Corolla")
my_car.display_info()
#car is a class
#my_car is an object of the car class
#brand and model are attriibute of the object
#display_info() is a method that displays the car's details
