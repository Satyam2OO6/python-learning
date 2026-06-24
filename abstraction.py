from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


# Child Class
class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


# Child Class
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button")


# Create objects
car = Car()
bike = Bike()

car.start()
bike.start()