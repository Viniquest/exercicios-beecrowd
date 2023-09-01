A, B = input().split()
A = int(A)
B = int(B)

if A <= B:
    resto = B % A
    if resto == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
else:
    resto = A % B
    if resto == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")        