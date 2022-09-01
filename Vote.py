class Error(Exception):
    """Base class for other exceptions"""
    pass

class belowAge(Exception):
    """Your age is below 18  you can't vote"""
    pass
try:
    age = int(input("Enter your age"))
    if (age<19):
        raise belowAge
except belowAge:
    print(belowAge.__doc__)
except Error:
    print("I am simply a error")
except ValueError:
    print("Invalide input")
else:
    print("You can vote")