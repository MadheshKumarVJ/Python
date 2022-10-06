class SetName(str):
    # def __init__(self,name):
    #     print(self)
    #     self.name=name
    #     for i in self:
    #         self[i]=i
     def __new__(cls,name) :
        IntegerName = (i  for i,letters in enumerate(name))
        print(type(IntegerName))
        for x  in IntegerName:
            print(x)
        print(type(IntegerName))
        return super().__new__(cls,IntegerName)




maddy = SetName("Maddy")
print(maddy)

# for x,y in enumerate("maddy"):
#     type(x)
#     print(x)