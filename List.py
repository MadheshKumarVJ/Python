print("TestPress Dev Team")
#list creation
employees=["Madhesh","karthik"]
#append in last
employees.append("Akash")
#insert in specific index
employees.insert(1,"Deepak")
#pop index (index not specified last element poped)
employees.pop(3)
#printing list
print(employees)
#iterating list
for employee in employees:
    print("Emp Name ",employee)
#index value pair
print(list(enumerate(employees)))
#slicing the list
print(employees[0:2])
#checking the presence 
if "Madhesh" in employees:
    print("Welocome Maddy")
