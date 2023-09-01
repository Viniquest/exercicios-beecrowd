tempo = int(input())
velocidade = int(input())

distancia = tempo * velocidade

gasto = distancia / 12
# 12 é o que o automóvel faz por litro, 12KM/L

print("{:.3f}".format(gasto))