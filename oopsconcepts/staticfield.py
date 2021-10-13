# statid field in a class example

class Student:
    # static fields/variables
    # which is common for every instance of object of a class
    major = "ECE"

    # contructor
    def __init__(self, rollno, name):
        # instance variables
        self.rollno = rollno
        self.name = name


s1 = Student(1, "Sindu")
s2 = Student(2, "Monika")

# instance variables needs an object to access them
# but static variables can be accessed directly
# using the class name
print(s1.rollno, s1.name, s1.major)
print(s2.rollno, s2.name, Student.major)
