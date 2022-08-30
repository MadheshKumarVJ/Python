class Triangle:
    def __init__(self,a,b,c) :
        self.a=a
        self.b=b
        self.c=c
    def perimeter(self):
        peri = self.a+self.b+self.c
        return peri
t1 = Triangle(1,2,3)
print(t1.perimeter())