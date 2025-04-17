class Vehicle:
    def move(self):
        print("This vehicle moves... somehow.")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road.")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on water.")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky.")

# Create a list of vehicles
vehicles = [Car(), Boat(), Plane()]

# Demonstrate polymorphism
for v in vehicles:
    v.move()
