def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

print(foo(3, 5))
print(foo('hello'))
print(foo('hello', 1, 2, 3))
print(foo('hello',1, 2, 3, key1='value', key2=777))


# V2

def foo(x, *args, **kwargs):
    args['surname'] = 'Paes'
    kwargs['name'] = 'Alex'
    new_args = args + ('extra', )
    bar(x, *new_args, **kwargs)

# -----------------------------------------------------

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return (f'{self.color}, {self.mileage}')


class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'
        # Uncomment line below + comment super()...
        # self.mileage = 300


print(Car('pink', 100))
print(AlwaysBlueCar('', 100))

car = Car('pink', 100)

print(Car)
print(car.__init__)

print(car.__repr__)
print(repr(car))

print(car.__str__)

blue_car = AlwaysBlueCar('pink', 100)
print(blue_car.__repr__)
print(blue_car.__str__)