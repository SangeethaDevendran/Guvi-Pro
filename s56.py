ppa=int(input())
qqa=list(map(int,input().split()))
a3a=0
b3a=0
qqa.sort(reverse=True)
for i in qqa:
  qqa=a3a+i
  if b3a>qqa:
    a3a=qqa
  else:
    a3a=b3a
    b3a=qqa
print(a3a,b3a)
