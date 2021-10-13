# Assignment on Abstraction concept

# Importing from abc module
from abc import abstractmethod, ABC


# Parent abstract module
class TouchScreenLaptop(ABC):

    # defining the abstract method
    # marked with decorator
    @abstractmethod
    def scroll(self):
        pass

    # defining the abstract method
    # marked with decorator
    @abstractmethod
    def click(self):
        pass


# Abstract Class
class HP(TouchScreenLaptop):
    # implementing the abstract method
    def scroll(self):
        print("HP Scroll")


# Abstract Class
class Dell(TouchScreenLaptop):
    # implementing the abstract method
    def scroll(self):
        print("Dell Scroll")


# class that provides the actual implementations
class HPNotebook(HP):
    # Implementation of Abstract method
    def click(self):
        print("HP Click")

    # Overriding the scroll method
    def scroll(self):
        # invoking the same method from it's parent class
        super().scroll()
        print("HPNotebook Scroll")


# class that provides the actual implementations
class DellNotebook(Dell):
    # Implementation of Abstract method
    def click(self):
        print("Dell Click")


# Duck Typing - Dependency Injection
class CallFunctions:

    # Injecting Object as a parameter
    def __init__(self, fobj):
        self.fobj = fobj

    # Invoking methods using the pass-in object
    def callfun(self):
        self.fobj.click()
        self.fobj.scroll()


# creating the Objects
hpnb = HPNotebook()
dellnb = DellNotebook()

# dynamically injecting the obj to a class
hp = CallFunctions(hpnb)
hp.callfun()

# dynamically injecting the obj to a class
dell = CallFunctions(dellnb)
dell.callfun()
