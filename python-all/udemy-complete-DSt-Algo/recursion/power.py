def power(base, exp):
    assert exp >= 0 and int(exp) == exp, 'exp must be int'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base, exp-1)


pw = power(2,4)
print(pw)

# or directly as below:
# print(power(2,4))