# Constructor(init method) of a class takes parameters into it

class Course:

    # parameterized constructor
    # inbuilt keyword "self" stores the memory of its object
    def __init__(self, name, ratings):
        # instance variables inside a contructor
        self.name = name
        self.ratings = ratings

    # Instance function to access instance variables that are in the contructor
    def display(self):
        print(self.name, self.ratings)

    # defining instance method and
    # calculating the average of the ratings
    def avg_rating(self):
        return sum(self.ratings)/len(self.ratings)

c1 = Course("Maths -", [3, 4, 5, 4, 3, 4, 3, 4, 4, 4.5])
c2 = Course("Physics -", [4, 5, 5, 4.5])
c1.display()
print(c1.avg_rating())
c2.display()
print(c2.avg_rating())



"""
# programmer class with accessor and mutator methods
class Programmer:

    # mutator/setter method inside with a variable is defining and assigning
    def setName(self, name):
        self.name = name

    # accessor/getter method to access a name field
    def getName(self):
        return self.name

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setTechnologies(self, technologies):
        self.technologies = technologies

    def getTechnologies(self):
        return self.technologies


p1 = Programmer()
p1.setName("Venkat")
p1.setSalary(10000000)
p1.setTechnologies(["java", "python", "html"])
print(p1.getSalary(), p1.getName(), p1.getTechnologies())"""