"""
    Iterate With enumerate() Instead of range()
"""

# FizzBuzz range()

numbers = [45, 22, 14, 65, 97, 72]
for i in range(len(numbers)):
    if numbers[i] % 3 == 0 and numbers[i] %5 == 0:
        numbers[i] = 'fizzbuzz'
    elif numbers[i] % 3 == 0:
        numbers[i] = 'fizz'
    elif numbers[i] % 5 == 0:
        numbers[i] = 'buzz'
    
print(numbers)


# FizzBuzz enumerate()

numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers):
    if numbers[i] % 3 == 0 and numbers[i] %5 == 0:
        numbers[i] = 'fizzbuzz'
    elif numbers[i] % 3 == 0:
        numbers[i] = 'fizz'
    elif numbers[i] % 5 == 0:
        numbers[i] = 'buzz'
    
print(numbers)


# enumerate() with its start param

numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers, start=52):
    print(i, num)