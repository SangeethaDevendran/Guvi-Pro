cha,cho,che,chi= map(int, input().split())
count=0
doa=cho-che
if (doa>=0):
    soa=(cha-che)*2
    for i in range(chi):
        if (i==chi-1):
             soa=soa/ 2
        if (doa<soa):
            doa=cho
            count+=1
        doa=doa-soa
        if (doa < 0):
            count=-1
            break
        s=2*cha-soa
    print(count)
else:
    print(-1)
