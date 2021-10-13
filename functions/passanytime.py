# Any parameter type can be passed into a function

# defining function print_report
# passing marks as sequence of type list : lst
# default marks list
def print_report(lst=[95.0, 96.0, 99.0]):

    # defining function inside function
    def subjects():
        # local variable : courses
        courses = ("maths", "physics", "chemistry")
        print(courses[lst.index(i)], " - ", i)

    def greetings():
        print("Congratulations!!")

    def wishes():
        return "Best of Luck!!"

    print(studentName, "'s Report Card!")
    for i in lst:
        # calling internal/nested function
        subjects()

    greetings()

    # returning a function
    return wishes


# global variable of type string: studentName
studentName = input("Enter student's Name : ")

# global sequence of type list : marks
marks = [float(x) for x in input("Enter marks please : ").split()]

# one way is
# calling a function by passing a list
# print_report(marks)

# another way is
# assigning a function to a variable
functionVariable = print_report

if len(marks) == 0:
    # calling a function without passing arguments
    a = functionVariable()
else:
    # and calling a function by passing an argument
    a = functionVariable(marks)
print(a())
