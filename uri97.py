i=1
intialval=7
while i<=9:
    count=0
    j=intialval
    while True:
        print("I=%d J=%d"%(i,j))
        count=count+1
        j=j-1
        if(count==3):
            break
    
    i=i+2
    intialval=intialval+2
    