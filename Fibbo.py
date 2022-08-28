print("Fibbionic series")
num = int(input("Enter a number"))
memo = [0,1]


def findN(n,memo):
    result=0
    if (n<len(memo)):
        return memo[n]
    elif(n==1 or n==2):
        result =1
    else:
        result = findN(n-1,memo)+findN(n-2,memo)
    memo.append(result)
    return result


print(findN(num-1,memo))