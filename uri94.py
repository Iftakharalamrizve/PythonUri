n=int(input())
list=[]
C_count=0
R_count=0
S_count=0
total=0
for i in range(0,n):
    valueGet=input().split(" ")
    animal,Identiy=valueGet
    animal=int(animal)
    if Identiy=='C':
        C_count=C_count+animal
        total=total+animal
    if Identiy=='R':
        R_count=R_count+animal
        total=total+animal
    if Identiy=='S':
        S_count=S_count+animal
        total=total+animal
print("Total: %d cobaias" %total)
print("Total de coelhos: %d" %C_count)
print("Total de ratos: %d" %R_count)
print("Total de sapos: %d" %S_count)
print("Percentual de coelhos: {:.2f} %".format((C_count/total)*100))
print("Percentual de ratos: {:.2f} %".format((R_count/total)*100))
print("Percentual de sapos: {:.2f} %".format((S_count/total)*100))