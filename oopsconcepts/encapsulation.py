# Encapsulation : data and code in single unit
# creating private fields and name mangling

class Student:

    def __init__(self):
        # instance variables - any object can access them
        self.id = 123
        # private variables are hidden variables and cannot be accessed directly by the object
        self.__name = "John"

    # instance accessor/getter method
    def getName(self):
        return self.__name

    # Instance variable
    def display(self):
        print(self.__name)


s = Student()

# object "s" can directly access the instance variable "id"
print(s.id)

# object "s" cannot access the private variable directly
# print(s.__name) doesn't work
# but "s" object can access the private varialbe indirectly
# either using Name Mangling syntax
print(s._Student__name)

# or using the methods of the object
print(s.getName())
s.display()
