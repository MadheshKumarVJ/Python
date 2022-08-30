#creating class
from Human import Human
from Programmer import Programmer


class TestPressEmployee(Human,Programmer):
    #constructor is called when the object is created
    def __init__(self,name) :
        self.name = name
        super().__init__(self.name)
        print(self.name)
    def BussinessTeam(self):
        return "Bussiness Team"
    def DeveloperTeam(self):
        return "Developer"
    def __str__(self):
        return "This is {}".format(self.name)

#creating object
Madhesh = TestPressEmployee("Madhesh kumar")
Bhuvi =TestPressEmployee("Bhuvi")
Karthik = TestPressEmployee("Karthik")
#refering values
Madhesh.DeveloperTeam()
Bhuvi.BussinessTeam()
Madhesh.code()
#printing object
print(Madhesh)
print(Karthik)
#Madhesh.live()
Maddy = Programmer("maddy")
Maddy.code()
