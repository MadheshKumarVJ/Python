class A():
    def say(self):
        super().say()

class B:
    def say(self):
        print("from B")

class C(A,B):
    def say(self):
        super().say()
call = C()
call.say()
print(C.mro())