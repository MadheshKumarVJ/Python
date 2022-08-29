print("Testpress employees name & id")
#creating a dictionary
dict={1:"Madhesh",2:"Karthik",3:"Akash"}
print(dict.get(9)) #return none
#print(dict[9]) throw err
#reassigned with key ref
dict[3]="AkashKumar"
#add new element
dict[4]="bhuvi"
#remove
dict.pop(4)
#update
updateEmp={4:"Bhuvi"}
dict.update(updateEmp)
print(dict)
print(dict.keys())
print(dict.values())
