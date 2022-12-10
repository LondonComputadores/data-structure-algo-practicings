def sumOfDigits(n):
    assert n>=0 and int(n) == n, 'The number must be int only'
    if n == 0:
        return 0
    return int(n%10) + sumOfDigits(int(n//10))
print(sumOfDigits(1111))
print(sumOfDigits(1234))