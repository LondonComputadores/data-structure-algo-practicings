from collections import ChainMap

dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain = ChainMap(dict1, dict2)

print(chain)
print(chain['three'])
print(chain['one'])
print(chain['missing'])


# Output:
# ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})
# 3
# 1
# Traceback (most recent call last):
#   File "chainmap_dict.py", line 10, in <module>
#     print(chain['missing'])
#   File "/usr/lib/python3.8/collections/__init__.py", line 898, in __getitem__
#     return self.__missing__(key)            # support subclasses that define __missing__
#   File "/usr/lib/python3.8/collections/__init__.py", line 890, in __missing__
#     raise KeyError(key)
# KeyError: 'missing'