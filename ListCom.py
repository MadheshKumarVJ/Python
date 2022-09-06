#creating a list with name and age
name= [["Madhesh",22],["Deepak",24],["Karthik",24],["kicha",17]]
"""in the deatills list 
i am returnig a list consits of ther suffix, name , age and their details using method(comprehension) """
sufffix = ["Mr " , "Master "]
deatils=[[sufffix[0],x[0],x[1]]   if x[1]>=18 else [sufffix[1],x[0],x[1]] for x in name ]
print(deatils)