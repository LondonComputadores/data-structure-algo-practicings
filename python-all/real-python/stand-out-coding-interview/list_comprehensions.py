"""
    Use List Comprehensions intead of map() and filter()
"""

# map() vs list comprehensions

# map()
numbers = [4,2,1,6,9,7]
def square(x):
    return x * x
print(list(map(square, numbers)))

# list comprehensions
print([square(x) for x in numbers])


# filter() vs list comprehensions

# filter()
def is_odd(x):
    return bool(x % 2)
print(list(filter(is_odd, numbers)))

# list comprehensions
print([x for x in numbers if is_odd(x)])
# for other booleans result formats
print([is_odd(x) for x in numbers])
print([is_odd(x) for x in numbers if is_odd(x)])
