# First Class

class Product:

    # contructor
    # __init__ method contructs an object of this class
    # self is a inbuilt keyword
    # to which memory location of the current object is being assigned
    def __init__(self):
        # Defining the fields: the instance Variables for this class
        self.name = "IPhone"
        self.description = "Its Awesome"
        self.price = 10000
    def firstfunction(self):
        print("This is first function!")
        print(self.name)

# p1 is the object of class Product
p1 = Product()
print(p1.name)
p1.firstfunction()
