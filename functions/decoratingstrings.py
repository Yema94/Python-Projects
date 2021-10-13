# function that decorate strings
# hello function is decorated with decor function

def whereabouts(fun):
    def whereareyou(n):
        return fun(n) + "\nWhere are you?"
    return whereareyou


# decorator function
def howabouts(fun):
    def howareyou(n):
        return fun(n)+"\nHow are you?"
    return howareyou



@howabouts # marking this hello function to the decor function
@whereabouts
def hello(name):
    return "Hello, " + name


print(hello("Raghav"))
