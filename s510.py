cha=int(input())
cho,che=3,3
while cha > 0:
    if cho==0:
        che*=2
        cho=che
    if cha==1:
        print(cho)
        break
    cha-=1
    cho-=1
