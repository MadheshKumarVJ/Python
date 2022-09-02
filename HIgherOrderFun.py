def say_name(name):
    return "Hello {} Welcome! ".format(name)
def say_age(age):
    return "Your age is {}".format(age)
def say_something(fun,x):
    something = fun(x)
    return something
print(say_something(say_name,"Madhesh Kumar V J"))
print(say_something(say_age,22))