A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

pi = 3.14159

areaTri = (A * C) / 2
areaCirc = pi * (C**2)
areaTrap = ((A + B ) * C) / 2
areaQuad = B**2
areaRet = A * B

print("TRIANGULO: {:.3f}".format(areaTri))
print("CIRCULO: {:.3f}".format(areaCirc))
print("TRAPEZIO: {:.3f}".format(areaTrap))
print("QUADRADO: {:.3f}".format(areaQuad))
print("RETANGULO: {:.3f}".format(areaRet))