#creating class
class TestPressEmployee:
    #constructor is called when the object is created
    def __init__(self,name) :
        self.name = name
        print(self.name)
    def BussinessTeam(self):
        print("Bussiness Team")
    def DeveloperTeam(self):
        print("Developer")

#creating object
Madhesh = TestPressEmployee("Madhesh")
#refering values
Madhesh.DeveloperTeam()

Bhuvi =TestPressEmployee("Bhuvi")
Bhuvi.BussinessTeam()
