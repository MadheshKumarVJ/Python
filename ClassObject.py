#creating class
class TestPressEmployee:
    #constructor is called when the object is created
    def __init__(self,name) :
        self.name = name
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
#printing object
print(Madhesh)
print(Karthik)
