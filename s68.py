nt1=int(input())
liata=[]
at=nt1//2+nt1
for i in range(1,nt1+1):
    if i%2==0:
        liata.append(i)
for i in range(1,nt1+1):
    if i%2!=0:
        liata.append(i)
for i in range(1,nt1+1):
    if i%2==0:
        liata.append(i)
print(at)
print(*liata)
