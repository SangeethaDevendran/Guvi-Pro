cha,cho=map(str,input().split())
count=0
for i in range(0,len(cha)):
    for j in range(0,len(cho)):
        if cha[i]==cho[j]:
            count+=1
if count>=2:
    print("yes")
else:
    print("no")
