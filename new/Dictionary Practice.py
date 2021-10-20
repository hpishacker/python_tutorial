mymap={}
for i in range(7):
    mymap[i]= int(input('Enter the number'))
c=0
for j in mymap.values():
    if j%2==0:
        print(j,' is even number')
    else:
        c=c+1
y=max(mymap.values())
for (maxkey,k) in mymap.items():
    if k ==y:
        break
print('Total count of Odd numbers are:',c)
print('Max value is :',y)
print('Key of maximum value is:',maxkey)
