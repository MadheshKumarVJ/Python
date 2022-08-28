# if else if else

attendance = False;
print("Attendance")
check = input("Enter Y or N:")
if check=="Y" or check=="y":
    print("present")
elif check=="N" or check=="n":
    print("absent")
else:
    print("Enter a valide input")

#for loop
employees=["Madhesh","Deepak","karthi"]
print("printing Employee names")
for employee in employees:
    print(employee)
#while
flag = True
breaker = 5
while flag:
    print("Inside while")
    if breaker==5:
        break
#for and continue

for i in range(1,11):
    if i==3:
        continue
    print(i)

