salario = float(input())

novo_salario = 0
reajuste = 0
percentual = 0

if salario <= 400:
    novo_salario = salario * 1.15
    percentual = 15
elif 400 < salario <= 800:
    novo_salario = salario * 1.12
    percentual = 12
elif 800 < salario <= 1200:
    novo_salario = salario * 1.10
    percentual = 10
elif 1200 < salario <= 2000:  
    novo_salario = salario * 1.07  
    percentual = 7  
elif salario > 2000:
    novo_salario = salario * 1.04    
    percentual = 4

reajuste = novo_salario - salario

print("Novo salario: {:.2f}".format(novo_salario))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual:", percentual, "%")