# Assignment 11 : Exception Handling
# Create, Raise and Handle a Custom "InvalidPasswordException"
# Custom Exception : Password Length Validation


# Creating an exception
class InvalidPasswordLengthException(Exception):
    def __init__(self, msg):
        self.msg = msg


class InvalidPasswordTypeException(Exception):
    def __init__(self, msg):
        self.msg = msg


def password_validation(geheimzahl):
    if len(geheimzahl) < 8:
        # raising an exception
        raise InvalidPasswordLengthException("The password should have atleast"
                                             " 8 Characters")

    elif not geheimzahl.isalnum():
        raise InvalidPasswordTypeException("Special Characters are not allowed"
                                           " in the password!")


# Handling an exception
try:
    f = open("credentials.txt", "a")
    username = input("Enter Username: ")
    print("Hinweis: password must follow alpha-numeric format"
          "\nNo special Characters are allowed!")
    password = input("Enter password: ")
    password_validation(password)

except InvalidPasswordLengthException as obj:
    print(obj
          + "\nPlease try again to update your password!")

except InvalidPasswordTypeException as obj:
    print(obj
          + "\nPlease try again to update your password!")

else:
    f.write("Username: {} - Password: {}\n"
            .format(username.encode(), password.encode()))
    print("Password is being Updated successfully!")

finally:
    f.close()
    print("Thank You!")
