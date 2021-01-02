a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
c=[]
for i in range(0, len(b)):
    numberB = b[i]
    for i in range(0, len(a)):
        numberA = a[i]
        if(numberA == numberB):
            c.append(numberA)
            break
print(c)