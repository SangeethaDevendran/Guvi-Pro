cha,cho=map(str,input().split())
counts=0
for i in range(0,len(cha)):
    for j in range(0,len(cho)):
        if cha[i]==cho[j]:
            counts+=1
if counts>=2:
    print("yes")
else:
    print("no")
