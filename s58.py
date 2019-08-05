cha=int(input())
cho=[]
dop=cha//2+cha
for i in range(1,cha+1):
  if i%2==0:
    cho.append(i)
for i in range(1,cha+1):
  if i%2!=0:
    cho.append(i)
for i in range(1,cha+1):
  if i%2==0:
    cho.append(i)
print(dop)
print(*cho)
