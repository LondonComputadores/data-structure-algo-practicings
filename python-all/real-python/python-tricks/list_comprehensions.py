# List Comprehensions

# Example 1

# (values) = [(expression) for (value) in (collection)]

squares = [x * x for x in range(10)]
print(squares)

# As a for loop

# (values) = []
# for (value) in (collection):
#     (values).append(expression)

squares2 = []
for x in range(10):
    squares2.append(x*x)
print(squares2)

# ----------------------------------------------------------

# Example 2

even_squares = [x * x for  x in range(10) if x % 2 == 0]
print(even_squares)