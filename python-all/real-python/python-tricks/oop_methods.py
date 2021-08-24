class MyClass:
    
    # Can modify object instance state
    # Can modify class state
    def method(self):
        return 'instance method called', self

    # Can't modify object instance state
    # Can modify class state
    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    # Can't modify object instance state
    # Can't modify class state
    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()
print(obj)
obj.method()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())
print(MyClass)

#print(MyClass.method())  # This must raise a NameError...

# ----------------------------------------------------------

#V2

class Pizza:

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'

    @classmethod
    def margherita(cls):
        return cls(['cheese', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['cheese', 'tomatoes', 'ham', 'mushrooms'])

print(Pizza.margherita())
print(Pizza.prosciutto())


# @staticmethods is quite useless unless you want/need a method
# namespace that doesn't make any change instance neither class
# state.