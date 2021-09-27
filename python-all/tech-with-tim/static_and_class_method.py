class person:
    population = 50
    
    def __init__(self, name):
        self.name = name
        #self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age): # Might take or not take a param
        if age >= 18:
            return 'Adult'
        if age < 18:
            return 'ID Please!'

    def display(self):
        print(f'{self.name} is {self.age} years old.')


person = person('Alex')
print(person.getPopulation())
print(person.isAdult(8))

"""
    This code was found on:
    https://www.youtube.com/watch?v=pUGyU-hxw5E&list=PLzMcBGfZo4-nhWva-6OVh1yKWHBs4o_tv&index=2

    and it is a bit weird and had to fix it as the teacher's version
    didn't go well. Lol

    Decided to skip his tutorials for now (26/Sep/2021)

    This was more useful:
    python-all/real-python/python-tricks/oop_methods.py
"""