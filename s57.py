ssa=input().split()
g3=int(ssa[1])
m3=int(ssa[0])
ssa=[int(d) for d in ssa[0]]
h3=0
c3=1;
while h3==0:
    prod=c3*m3
    k=[int(d) for d in str(prod)]
    r=0
    j=len(k)-1
    while k[j]==0:
        r+=1
        j-=1
    if r>=g3:
        print(prod)
        h3=1
    c3+=1
