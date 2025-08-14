# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclasses
class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"

class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"

class Boat(Vehicle):
    def move(self):
        return "🚤 Sailing on water"

def start_vehicle(vehicle: Vehicle):
    print(vehicle.move())  # Print the returned string

# Polymorphic behavior
for vehicle in [Car(), Plane(), Boat()]:
    start_vehicle(vehicle)
