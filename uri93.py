list=[]
for i in range(0,5):
    value=int(input())
    list.append(value)
height_number=max(list)
index=list.index(height_number)
print(height_number)
print(index+1)