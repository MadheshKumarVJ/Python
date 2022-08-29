print("Dev Team Tuple")
#declaration of tuple
devTeam = ("Madhesh",["Karthik","Deepak"])
#print
print(devTeam)
#packing and unpacking
maddy = devTeam[0]
print(maddy)
#nested mutable elementch can be reassigned
devTeam[1][0]="Karthikeyan"
print(devTeam)
#tuple is immutable this throws err
#devTeam[0]="Maddy"
#concat(+)
testPress =devTeam+("Akash","Aravindh","bhuvi")
print(testPress)