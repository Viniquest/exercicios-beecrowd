i, f = input().split()
i = int(i)
f = int(f)

if i < f:
    tempo = f - i
    print("O JOGO DUROU", tempo, "HORA(S)")
else:
    tempo = 24 - i + f
    print("O JOGO DUROU", tempo, "HORA(S)")