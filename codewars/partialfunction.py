#One way
"""import functools

def greet(greeting, target):
    return f"{greeting}, {target}!"

greet = functools.partial(greet, "Hola")
print(greet('Bob'))"""

#other way

class Greet:
    def __init__(self, greeting):
        self.greeting = greeting

    def greet(self, target):
       self.target = target
       return self.greeting + ' ' + self.target


English = Greet('Hello')
print(English.greet('Yesh'))
