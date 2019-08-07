chaal,choal=map(int,input().split())
lists=list(map(int,input().split()))
caa=0
for i in lists:
    kaa=86400-i
    choal-=kaa
    caa+=1
    if choal<=0:
        break  
print(caa)
