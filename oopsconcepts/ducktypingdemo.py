class Duck:
    def talk(self):
        print("quack quack")


class Human:
    def talk(self):
        print("Hello")


# Kind of Duck typing because the same will do multiple things
# based on the obj we pass to it dynamically at run time.
def callTalk(obj):
    # method is being invoked irrespective of class
    obj.talk()

d = Duck()
# dynamically injecting an obj to a function
callTalk(d)

h = Human()
# dynamically injecting an obj to a function
callTalk(h)