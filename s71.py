cha=str(input())
cho=str(input())
T11=0
T21=0
Tato=""
for X in range(0,len(cha)):
    T11=ord(cha[X])-96
    T21=ord(cho[X])+T11
    if(T21>122):
        T21=T21-122
        T21=T21+96
    Tato=Tato+chr(T21)
print(Tato)
