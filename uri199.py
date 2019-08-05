n=int(input())
list=[]
for x in range(0,n):
    values=input().split(" ")
    first,second=values
    list.append([int(first),int(second)])
for slist in list:
    sum=0
    if(slist[0]<slist[1]):
        for y in range(slist[0]+1,slist[1]):
            if(y%2!=0):
                sum = sum+y
    elif slist[0]==slist[1]:
        sum=0
    else:
        for z in range(slist[1]+1,slist[0]):
            if(z%2!=0):
                sum = sum+z
    print(sum)
