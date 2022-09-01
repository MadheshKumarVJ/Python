
list =[1,2,3,4]

#to iter object both are valide 
Iterator = iter(list)
methodIte = list.__iter__()

#using next method or __next__()
print(next(methodIte))
print(methodIte.__next__())
print(next(methodIte))
print(methodIte.__next__())

#using next method or __next__()
print(next(Iterator))
print(Iterator.__next__())
print(next(Iterator))
print(Iterator.__next__())

#this throws a error because there is no such method exist in list 
#print(list.__next__())
