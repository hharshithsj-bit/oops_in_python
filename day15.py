
from abc import ABC, abstractmethod
# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Car class
class Car(Vehicle):

    def start(self):
        print("Car engine started!")

    def stop(self):
        print("Car engine stopped!")
# Bike class
class Bike(Vehicle):

    def start(self):
        print("Bike engine started!")

    def stop(self):
        print("Bike engine stopped!")

# Main program
car = Car()
bike = Bike()

print("----- CAR -----")
car.start()
car.stop()

print("\n----- BIKE -----")
bike.start()
bike.stop()
