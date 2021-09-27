def func(x=1):
    return x ** 2

call = func(5)
print(call)

def func(word, freq=1):
    print(word*freq)

call = func('alex', 5)

def func(word, add=5, freq=1):
    print(word*(freq+add))

call = func('alex', 5)

class car(object):
    def __init__(self, make, model, year, condition='New', kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll=True):
        if showAll:
            print(f'This car is {self.make} {self.model} from {self.year} with {self.kms} kms')
        else:
            print(f'This is a great {self.year} {self.make} {self.model}')

whip = car('Ford', 'F150', 2016, 'Second-hand', '<100k')
whip.display(True)