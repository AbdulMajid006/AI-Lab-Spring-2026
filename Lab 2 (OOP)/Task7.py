# Task#7:
# Vehicle System (Method Overriding – Polymorphism):
# Create a base class Vehicle with method start().
# Create subclasses Car, Bike, and Bus that override start().
# Create objects and call start() to observe polymorphism.

class Vehicle:
    def start(self):
        print("Vehicle is starting...")
        
class Car(Vehicle):
    def start(self):
        print("Car engine started.")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started.")

class Bus(Vehicle):
    def start(self):
        print("Bus engine started.")

v1 = Vehicle()
c1 = Car()
b1 = Bike()
bus1 = Bus()

print("Vehicle:")
v1.start()
print("Car:")
c1.start()
print("Bike:")
b1.start()
print("Bus:")
bus1.start()
