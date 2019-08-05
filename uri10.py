input1=input().split(" ")
input2=input().split(" ")
code1,qty1,price1=input1
code2,qty2,price2=input2
total=((int(qty1)*float(price1))+(int(qty2)*float(price2)))
print("VALOR A PAGAR: R$ %0.2f" % total)
