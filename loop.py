list=[]
list2=[]
for x in range(1,10,5):
    list.append(x)
for y in range(11,20,5):
    list2.append(y)
list=list+list2
print(list)