cha,cho=map(int,input().split())
lists=list(map(int,input().split()))
caa=0
for i in lists:
    kaa=86400-i
    cho-=kaa
    caa+=1
    if cho<=0:
        break  
print(caa)
