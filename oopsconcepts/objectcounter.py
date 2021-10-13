# Define a static field and static method
# count and display the num of objects for a particular class

class ObjectCounter:
    # static field
    numberOfObjects = 0

    # constructor
    def __init__(self):
        # accessing and incrementing the static variable
        ObjectCounter.numberOfObjects += 1

    @staticmethod # marking with decorator
    def displayCount():  # doesn't require "self"
        print(ObjectCounter.numberOfObjects)

o1 = ObjectCounter()
o2 = ObjectCounter()

ObjectCounter.displayCount()
