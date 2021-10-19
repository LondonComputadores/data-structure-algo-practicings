"""
    fibonacci 0,1,1,2,3,5,8,13,21,34,55,89...
"""
def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Must be positive int only'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))