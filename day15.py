
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass



class Car(Vehicle):

    def start(self):
        print("Car engine started!")

    def stop(self):
        print("Car engine stopped!")



class Bike(Vehicle):

    def start(self):
        print("Bike engine started!")

    def stop(self):
        print("Bike engine stopped!")


car = Car()
bike = Bike()

print("----- CAR -----")
car.start()
car.stop()

print("\n----- BIKE -----")
bike.start()
bike.stop()
