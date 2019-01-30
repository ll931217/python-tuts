myUniqueList = []
myLeftovers = []

def pushLeftovers(val):
    myLeftovers.append(val)

def push(val):
    if val in myUniqueList:
        pushLeftovers(val)
    else:
        myUniqueList.append(val)
    return myUniqueList

print(push(5))
print(push(7))
print(push(3))
print(push(4))
print(push(2))
print(push(3))
print(push(3))
print(push(1))
print(push(6))
print(push(6))
print(myLeftovers)
