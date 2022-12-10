# Working with just one asterisk * (* extracts the key)

def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y,z))

print_vector(0, 1, 0)

tuple_vec = (0, 1, 0)
list_vec = [1, 0, 1]

print_vector(tuple_vec[0], tuple_vec[1], tuple_vec[2])

print_vector(*tuple_vec)
print_vector(*list_vec)

gen_expr = ( x * x for x in range(3))
print_vector(*gen_expr)


# Workng with double asterisks ** (** extract the value of the key)

dict_vec = {'x': 1, 'y': 0, 'z': 6}

print_vector(**dict_vec)  # this must output the expect result

print_vector(dict_vec)  # this must output a TypeError