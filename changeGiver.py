import itertools

class NotIntegerError(ValueError): pass

def all_coins():
    zero = [0 for x in range(9)]
    one  = [1 for x in range(10)]
    two  = [2 for x in range(5)]
    five = [5 for x in range(2)]
    ten  = [10]
    coins=[zero,one,two,five,ten]
    total=[]
    for one in coins:
        total.extend(one)
    return total

def giveChange(money):
    assert int(money)<=10,"ask less there are more people other than you "
    coins = all_coins()
    realChange=set()
    changes = tuple(itertools.combinations(coins,int(money)))
    for change in changes:
        if sum(change)==int(money):
            realChange.add(change)
    return realChange

def invalideInput(self,val):
    if (val<=0):
        raise NotIntegerError("Enter valide amount if you change for negative values keep the money on the machine and ran away")
    self.give

if __name__=='__main__':          
    inr = input("Enter the amount to get change : ")
    count =0
    print("Your posiibilites are!!!")
    for possibility in giveChange(inr):
        count +=1
        print(count,".",possibility)
        ###