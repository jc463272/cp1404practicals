"""
CP1404 - William Hunter
New class unreliable car inherit from car class
Estimated: 20 mins
"""
from random import randint
from car import Car

class UnreliableCar(Car):
    """New class for unreliable car."""
    def __init__(self, reliability, **kwargs):
        """Initialise the instances for UnreliableCar."""
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance, if the car is reliable."""
        random_number = randint(0,100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance) #Use drive method from parent class drive
        return distance_driven
