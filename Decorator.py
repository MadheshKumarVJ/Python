#decorator
def oncam(fun):
    def inner(x):
        print("switching on camera")
        fun(x)
    return inner


#ordinary method
def cam(click):
    print(click)

photo = "Clicking image"
#decorating a ordinary method
cam = oncam(cam)
cam(photo)
