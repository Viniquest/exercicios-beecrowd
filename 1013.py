a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

maiorAB = (a + b + abs(a - b)) / 2

maior = (maiorAB + c + abs(maiorAB - c)) / 2

print(int(maior), "eh o maior")

maior2 = max(a, b, c)

print(int(maior2), "eh o maior")