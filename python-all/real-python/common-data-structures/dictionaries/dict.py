phonebook = {
    'bob': 7387,
    'alice': 3719,
    'jack': 7052,
}

squares = {x: x * x for x in range(6)}

print(phonebook)

print(phonebook.__reversed__())

print(phonebook['alice'])

print(squares)


# Output:
# {'bob': 7387, 'alice': 3719, 'jack': 7052}
# <dict_reversekeyiterator object at 0x7f867d519130>
# 3719
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}