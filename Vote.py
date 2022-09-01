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
    else:
        print("You can vote")
except belowAge:
    print(belowAge.__doc__)
