ppa, Qpa, Fpa, Kda = map(int, input().split())
cnta = 0
Dvda = Qpa-Fpa
if (Dvda >= 0):
    S11 = (ppa-Fpa)*2
    for X in range (Kda):
        if (X == Kda-1):
             S11 =S11/ 2
        if (Dvda < S11):
            Dvda= Qpa
            cnta += 1
        Dvda = Dvda - S11
        if (Dvda < 0):
            cnta = -1
            break
        S11 = 2*ppa - S11
    print (cnta)
else:
    print (-1)
