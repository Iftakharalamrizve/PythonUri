import math

a, b, c= input().split(" ")
result = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
resultfinal = (int(result) + int(c) + abs(int(result) - int(c)))/2
print("%d eh o maior" %resultfinal)