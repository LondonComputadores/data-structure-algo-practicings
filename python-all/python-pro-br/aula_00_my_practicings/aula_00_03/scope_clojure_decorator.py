"""
Este módulo não é parte deste curso de DStrc. da Python Pro Br
https://towardsdatascience.com/decorators-and-closures-by-example-in-python-382758321164
"""

def my_decorator(func):
    def closure():
        print("Before function call")
        func()
        print("After function call")

    return closure

# @my_decorator  # uncomment this only if line 22 is uncommented too
def say_hello():
    print("Hello World!")


if __name__ == "__main__":

    # hello = say_hello  # uncomment this only if line 14 is uncommented too
    hello = my_decorator(say_hello)
    hello()
    #print(__doc__)
