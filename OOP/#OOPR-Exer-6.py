#OOPR-Exer-6

class Vehicle:

    def __init__(self):
        self.mileage = 35
        self.fuel_left = 8

    def identify_distance_that_can_be_travelled(self):
        if self.fuel_left <= 5:
            return 0
        return (self.fuel_left - 5) * self.mileage

    def identify_distance_travelled(self, initial_fuel):
        initial_fuel -= self.fuel_left
        distance = initial_fuel * self.mileage
        return distance


car = Vehicle()
print("Distance that can be travelled :", car.identify_distance_that_can_be_travelled())
print("Distance travelled :", car.identify_distance_travelled(25))
