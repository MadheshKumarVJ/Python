print("testpress emp id")
#declaration of set
#mutable but cant add muttable datatypes
#set={1,2,3,4,5,6,7,1,2,4,[2,3]} err
set1={1,2,3,4,5,6,7,1,2,4}
print(set1)
#add element
set1.add(8)
#update multiple values
set1.update([10,11,12])
#remove value(err if not present)
set1.remove(11)
#discard value (no err)
set1.discard(11)
print(set1)
set2=set([12,13,14,15,1,3])
set3 = set1|set2 #union
set3 = set1&set2 #intersection
set3 = set1-set2 #diffrence
set3 = set1^set2 #symmetric diffrence
print(set3)

#frozen set immutable set
OwnerId=set([1,2])
ClientId = set([1,2,3])
OwnerId = frozenset(OwnerId)
ClientId = frozenset(ClientId)
print(OwnerId)
print(ClientId)
#frozen set methods
#makes a copy
Ownercpy=OwnerId.copy()
print(Ownercpy)
#insection
common = OwnerId.intersection(ClientId)
print(common)
# union
union = OwnerId.union(ClientId)
print(union)
# difference
diff = OwnerId.difference(ClientId)
print(diff)
# symmetric_difference
sydiff = OwnerId.symmetric_difference(ClientId)
print(sydiff)


print(OwnerId.issubset(ClientId))
print(ClientId.issuperset(OwnerId))
#nothing matches then print true
print(ClientId.isdisjoint(OwnerId))

