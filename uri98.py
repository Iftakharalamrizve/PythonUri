i=0;
while i<=2:
    for j in range(1,4):
        i=round(i, 2)
        j=j+i
        test=int(i)
        valid=str(test)+'.'+str(0)
        if str(i)==valid or i==0:
            print("I=%d J=%d"%(i,j))
        else:
            print("I=%0.1f J=%0.1f"%(i,j))
    i=i+.2 