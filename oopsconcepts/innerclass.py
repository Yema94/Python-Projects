# create a class inside another class

class Car:

    def __init__(self, make, year):
        self.make = make
        self.year = year

    class Engine:

        def __init__(self, number):
            self.number = number

        def start(self):
            print("Engine started!", self.number)


c = Car("BMW", 2017)
e = c.Engine("aldk234k334k")
print(c.make, c.year, e.number)
e.start()
