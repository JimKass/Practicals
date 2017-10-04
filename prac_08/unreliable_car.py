"""

"""

from random import randint
from prac_08.car import Car

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return "{}, fuel={}, odometer={}, {}% reliable".format(self.name, self.fuel, self.odometer, self.reliability)

    def drive(self, distance):
        is_working = self.reliability > randint(0, 101)
        if is_working:
            super().drive(distance)
        else:
            return 0
