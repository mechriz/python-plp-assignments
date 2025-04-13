# Assignment 1: Design Your Own Class

# Base class
class Character:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def show_info(self):
        print(f"{self.name} has the power of {self.power}.")

# Subclass (Inheritance + Encapsulation)
class Superhero(Character):
    def __init__(self, name, power, secret_identity):
        super().__init__(name, power)
        self.__secret_identity = secret_identity  # Encapsulated (private)

    def reveal_identity(self):
        print(f"{self.name}'s secret identity is {self.__secret_identity}.")


      
#  Activity 2: Polymorphism Challenge

class Car:
    def move(self):
        print("Driving on the road 🚗")

class Plane:
    def move(self):
        print("Flying in the sky ✈️")

class Boat:
    def move(self):
        print("Sailing on the water 🚤")
