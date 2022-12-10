# String Conversion "__repr__" vs "__str__"

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # V1
    # def __str__(self):
    #     return 'a {self.color} car'.format(self=self)

    # V2
    # def __repr__(self):
    #     return '__repr__ for Car'
    
    # def __str__(self):
    #     return '__str__ for Car'

    # V3
    def __repr__(self):
        return '{self.__class__.__name__}({self.color}, \
                 {self.mileage})'.format(self=self)

my_car = Car('red', 37281)
print(my_car)

print(str(my_car))
print(str([my_car]))

print('{}'.format(my_car))

# ------------------------------------------------------

import datetime

today = datetime.date.today()

print(str([today, today, today]))

print(str(today))
print(repr(today))