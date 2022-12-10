"""
    Intead of %s %d or {}.format(), use:
    f'{variable/param} directly only!'
"""
# Python 3.9

def get_name_and_decades(name, age):
    return "My name is {} and I'm {}/10:.5f old." % format('Maria', 31)
print(get_name_and_decades)
# Out: <function get_name_and_decades at 0x7f...>


def get_name_and_decades(name, age):
    return "My name is {} and I'm {}/10:5f old.".format('Maria', 31)
print(get_name_and_decades)
# Out: <function get_name_and_decades at 0x7f...>


# Using the f'string formatting with :.f formatting
def get_name_and_decades(name, age):
    return f"My name is {name} and I'm {age / 10:5f} decades old."
print(get_name_and_decades('Maria', 31))
# Out: My name is Maria and I'm 3.100000 decades old.