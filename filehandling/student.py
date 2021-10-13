# test module/class to work on pickle module
# pickle serialization means dumping an object into a file

class Student:
    def __init__(self, id, name, testscore):
        self.id = id
        self.name = name
        self.testscore = testscore

    def display(self):
        print(self.id, self.name, self.testscore)