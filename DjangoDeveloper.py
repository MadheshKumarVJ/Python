import datetime

class DjangoDeveloper:

    def __init__(self,name,address,date_of_joining) :
        self.name = name
        self.languageKnown = "Python"
        self.domain = "Web Development"
        self.address = address
        self.date_of_joining = date_of_joining
        self.status={}
        self.comments={}

    def checkMonday(self,date = datetime.datetime.today()):
       flag = False
       day_count= datetime.datetime.today().weekday()
       if day_count==0:
            flag=True
       return flag

    def addStatus(self,status):
        reviewCount = len(status)+1 
        topicsCovered = input("Enter topics coverd : ")

        status[reviewCount] = topicsCovered
        print(status)
        return status

        
    def addComments(self,comments):
        commentCount = len(comments)+1 
        comment = input("Enter Your Comment : ")

        comments[commentCount] = comment
        return comments

    def tranningModule(self):
        if self.checkMonday():
            self.addStatus(self.status)
            self.addComments(self.comments)
    
    