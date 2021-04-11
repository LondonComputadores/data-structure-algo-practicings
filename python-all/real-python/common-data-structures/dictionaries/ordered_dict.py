import collections

d = collections.OrderedDict(one=1, two=2, three=3)
print(d)

d['four'] = 4
print(d)

print(d.keys())


# Output:
# OrderedDict([('one', 1), ('two', 2), ('three', 3)])
# OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
# odict_keys(['one', 'two', 'three', 'four'])