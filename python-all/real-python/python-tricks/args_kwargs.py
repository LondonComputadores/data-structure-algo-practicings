def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

#print(foo())
print(foo('hello'))
print(foo('hello', 1, 2, 3))
print(foo('hello',1, 2, 3, key1='value', key2=777))


# V2

def foo(x, *args, **kwargs):
    kwargs['name'] = 'Alex'
    new_args = args + ('extra', )
    bar(x, *new_args, **kwargs)

# -----------------------------------------------------

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'