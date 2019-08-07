tvs,sunt = map(int,input().split())
veeta = list(map(int,input().split()))
bht,neet = 0,[]
for i in range(0,len(veeta)):
  tvs= i
  for p in range(0,len(veeta)):
    for l in range(0,sunt):
      if l == sunt-1:
        try:
          bht += veeta[p+i]
        except IndexError:
            tvs = tvs-1
            bht +=veeta[tvs]
      else:
        bht += veeta[i]
    neet.append(bht)
    bht = 0
for i in range(0,len(veeta),sunt):
  bht = sum(veeta[i:i+sunt])
  neet.append(bht)
print(*sorted(set(neet)))
