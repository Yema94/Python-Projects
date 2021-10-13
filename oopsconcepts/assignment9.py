# Defining Class
class Patient:

    # Contructor
    def __init__(self):
        # Private variables of type None
        self.__id = None
        self.__name = None
        self.__ssn = None

    # Mutator to set ID
    def setId(self, id):
        # assigning to a private variable
        self.__id = id

    # Accessor method
    def getId(self):
        # returning the private variable
        return self.__id

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSSN(self, ssn):
        self.__ssn = ssn

    def getSSN(self):
        return self.__ssn


# creating an object to a class
p = Patient()
p.setId("Patient Id Number")
p.setName("Patient Name")
p.setSSN("Patient Social Security Number")
print(p.getId())
print(p.getName())
print(p.getSSN())
