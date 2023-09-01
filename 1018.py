valor = int(input())

print(valor)

valor100 = valor / 100
resto100 = valor%100
print(int(valor100), "nota(s) de R$ 100,00")

valor50 = resto100 / 50
resto50 = resto100%50
print(int(valor50), "nota(s) de R$ 50,00")

valor20 = resto50 / 20
resto20 = resto50%20
print(int(valor20), "nota(s) de R$ 20,00")

valor10 = resto20 / 10
resto10 = resto20%10
print(int(valor10), "nota(s) de R$ 10,00")

valor5 = resto10 / 5
resto5 = resto10%5
print(int(valor5), "nota(s) de R$ 5,00")

valor2 = resto5 / 2
resto2 = resto5%2
print(int(valor2), "nota(s) de R$ 2,00")

print(int(resto2), "nota(s) de R$ 1,00")