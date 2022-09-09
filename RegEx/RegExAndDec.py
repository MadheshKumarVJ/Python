import re
def checkMadhesh(name):
    return re.search(r"^M.*h$",name)
def applyKumar(name):
   return re.sub("$"," Kumar",name)
   
def checkDeepak(name):
    return re.search(r"^D.*k$",name)
def applyAadhiShankar(name):
    return re.sub("$"," AadhiShankar",name)


def addLastName(fun):
    def inner(rules,firstName):
        a=0
        for check,apply in rules:
            if check(firstName):
                print(apply(firstName))
                fun(rules,firstName,True)
                break
            else:
                a=a+1
                print(a," iteration")
                fun(rules,firstName)
    return inner

rules=((checkMadhesh,applyKumar),(checkDeepak,applyAadhiShankar))
# madhesh = addLastName(rules)
# madhesh("Madhesh")
# deepak = addLastName(rules)
# deepak("Deepak")

@addLastName
def name(rules,name,flag=False):
    if flag:
        print("Last name found")
    else:
        print("Last name not found")

#names = addLastName(name)

yourName=input("Enter a name to find last name")
name(rules,yourName)
