# list: Mutable Dynamic Arrays

arr = ['one', 'two', 'three']
print(arr[0])

# Lists have a nice repr
print(arr)

# List are mutable
arr[1] = 'hello'
print(arr)

del arr[1]
print(arr)

# Lists can hold arbitrary data types
arr.append(23)
print(arr)