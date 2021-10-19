def solution(s):
    c = s[0]
    if c.isupper():
        return 'upper'
    elif c.islower():
        return 'lower'
    elif c.isdigit():
        return 'digit'
    else:
        return 'other'

print(solution('DIGIT'))
print(solution('digit'))
print(solution('1Digit'))
print(solution('@digit'))