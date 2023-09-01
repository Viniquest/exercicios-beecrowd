valor = float(input())

print("NOTAS:")

nota100 = valor / 100
resto100 = valor%100
print(int(nota100), "nota(s) de R$ 100.00")

nota50 = resto100 / 50
resto50 = resto100%50
print(int(nota50), "nota(s) de R$ 50.00")

nota20 = resto50 / 20
resto20 = resto50%20
print(int(nota20), "nota(s) de R$ 20.00")

nota10 = resto20 / 10
resto10 = resto20%10
print(int(nota10), "nota(s) de R$ 10.00")

nota5 = resto10 / 5
resto5 = resto10%5
print(int(nota5), "nota(s) de R$ 5.00")

nota2 = resto5 / 2
resto2 = resto5%2
print(int(nota2), "nota(s) de R$ 2.00")

valorM = (valor - valor//1) * 100

print("MOEDAS:")

moeda100 = valorM / 100
resto1 = valorM%100
print(int(resto2), "moeda(s) de R$ 1.00")

moeda50 = resto1 / 50
restoM50 = resto1%50
print(int(moeda50), "moeda(s) de R$ 0.50")

moeda25 = restoM50 / 25
resto25 = restoM50%25
print(int(moeda25), "moeda(s) de R$ 0.25")

moeda10 = resto25 / 10
restoM10 = resto25%10
print(int(moeda10), "moeda(s) de R$ 0.10")

moeda5 = restoM10 / 5
restoM5 = restoM10%5
print(int(moeda5), "moeda(s) de R$ 0.05")

print(int(restoM5), "moeda(s) de R$ 0.01")