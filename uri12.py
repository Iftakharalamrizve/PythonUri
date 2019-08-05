pi = 3.14159
getVal=input().split(" ")
a,b,c=getVal

triangular=(float(a)*float(c))/2
CIRCULO=(float(c)*float(c))*pi
TRAPEZIO=(((float(a)+float(b))/2)*float(c))
QUADRADO=((float(b)*float(b)))
RETANGULO=((float(a)*float(b)))

print("TRIANGULO: %0.3f"%triangular)
print("CIRCULO: %0.3f"%CIRCULO)
print("TRAPEZIO: %0.3f"%TRAPEZIO)
print("QUADRADO: %0.3f"% QUADRADO)
print("RETANGULO: %0.3f"% RETANGULO)
