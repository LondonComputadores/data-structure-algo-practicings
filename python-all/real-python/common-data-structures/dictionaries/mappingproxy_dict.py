from types import MappingProxyType

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)

#The proxy is read-only now:
read_only['one']
print(read_only)

# Updates to the original are reflected in the proxy:
writable['one'] = 42
print(read_only)

#This will raise an error:
read_only['one'] = 23
print(read_only)