cha,cho,che,chi=map(int,input().split())
lists=list(map(int,input().split()))
sha=[]
for i in range(0,len(lists)):
    for j in range(i,len(lists)):
        for k in range(j,len(lists)):
            sha.append(cho*lists[i]+che*lists[j]+chi*lists[k])
print(max(sha))
