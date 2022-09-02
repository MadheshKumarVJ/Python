#decorator
def oncam(fun):
    def inner(x):
        print("----switching on camera----")
        fun(x)
    return inner
def offcam(fun):
    def inner(x):
        fun(x)
        print("----switching off cam----")
    return inner

#using @decmethod insted of cam=oncam(cam)

#ordinary method
#using two decorators
@oncam
@offcam
def cam(click):
    print(click)

photo = "  **Clicking image**"

#decorating a ordinary method @ plays its role here
cam(photo)
