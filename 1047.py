hi, mi, hf, mf = input().split()
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

if hi < hf and mi < mf:
    tempoH = hf - hi
    tempoM = mf - mi
    print("O JOGO DUROU", tempoH, "HORA(S) E", tempoM, "MINUTO(S)")
elif hi < hf and mi > mf:
    tempoH = hf - hi - 1
    tempoM = 60 - mi + mf
    print("O JOGO DUROU", tempoH, "HORA(S) E", tempoM, "MINUTO(S)")
elif hi > hf and mi > mf:
    tempoH = 24 - hi + hf - 1
    tempoM = 60 - mi + mf
    print("O JOGO DUROU", tempoH, "HORA(S) E", tempoM, "MINUTO(S)")
elif hi > hf and mi < mf:
    tempoH = 24 - hi + hf
    tempoM = mf - mi
    print("O JOGO DUROU", tempoH, "HORA(S) E", tempoM, "MINUTO(S)")
elif hi == hf and mi == mf:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif hi == hf:
    if mi > mf:
        tempoM = 60 - mi + mf
        print("O JOGO DUROU 23 HORA(S) E", tempoM, "MINUTO(S)")
    if mi < mf:
        tempoM = mf - mi
        print("O JOGO DUROU 0 HORA(S) E", tempoM, "MINUTO(S)")    
