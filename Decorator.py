#decorator
def oncam(fun):
    def inner(x):
        print("switching on camera")
        fun(x)
    return inner


#using @decmethod insted of cam=oncam(cam)
@oncam
#ordinary method
def cam(click):
    print(click)

photo = "Clicking image"

#decorating a ordinary method @ plays its role here
cam(photo)
