a = [1,1,2,3,5,8,13,21,34,55,89,100]
for i in range(0,12):
    if(a[i]<5):
        print('a['+str(i)+'] = '+str(a[i]) + ' < 5')

print('===============================')

for elem in a:
    if elem < 5:
        print(elem)
