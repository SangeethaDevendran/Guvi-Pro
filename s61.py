def charming(loi):
        bob=1        
        for p in range(0,len(loi)-1):
                if loi[p]!=loi[p+1]:
                        bob=bob+1
                else:
                    break
        return bob
cha=int(input())
cho=list(map(int,input().split()))
for p in range(0,len(cho)):
        if cho[p]>0:
                cho[p]=1
        else:
             cho[p]=0
che=""
for p in range(0,len(cho)):
        baba=cho[p::]
        che=che+str(charming(baba))+" "
print(che.strip())
