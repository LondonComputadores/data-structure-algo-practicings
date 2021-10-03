sort_num = sorted([6,5,3,7,2,4,1])
print(sort_num)

sort_str_list = sorted(['cat', 'dog', 'cheetah', 'rhino', 'bear'], reverse=True)
print(sort_str_list)

animals = [
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5},
]
sort_animals = sorted(animals, key=lambda animal: animal['age'])
print(sort_animals)