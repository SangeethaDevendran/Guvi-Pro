import sys
def palindromeha(cha):
    if len(cha) == 1:
        return False
    if cha == cha[::-1]:
        return True
    return False
cha = input()
che = len(cha)
for i in range(che-1, 0, -1):
    for j in range(0, che-i):
        i1 = j
        i2 = j+i+1
        dop = cha[i1:i2]
        if palindromeha(dop):
            print(che-len(dop))
            sys.exit()
