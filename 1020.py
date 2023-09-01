dias = int(input())

anos = dias//365
dias = dias%365

meses = dias//30
dias = dias%30

print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")