def fibonacci_function(a,b,c,value):
    print(c)
    a=b
    b=c
    c=a+b
    if value>1:
        fibonacci_function(a,b,c,value-1)
fibonacci_function(0,1,0,10)