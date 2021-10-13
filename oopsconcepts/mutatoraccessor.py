# Mutator/Setter method and Accessor/Getter method

class Student:

    # mutator
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id


s = Student()
s.setId(12)
print(s.id) # one method to access the variables of a class
print(s.getId())   # another method
