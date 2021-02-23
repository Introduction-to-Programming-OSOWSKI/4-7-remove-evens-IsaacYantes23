def removeEvens(k):
    newList = k
    numPop = 0
    for i in range(0,len(k)):
        if k[i -numPop] % 2 == 0 and newList[i - numPop] != 0:
            newList.pop(i -  numPop)
            numPop = numPop + 1
            
    return newList

print(removeEvens([1,2,3,4,5,66,8,8]))
