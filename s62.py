import sys, string, math

nunt1 = 4
Laata = []
for i in range(0,nunt1) :
    Laata.append([])
Lt2 = []
for i in range(0,nunt1) :
   Laata[i] = [ int(x) for x in input().split()]
xt1 = Laata[0][0]
yt1 = Laata[0][1]
for i in range(1,nunt1) :
    if Laata[i][0] != xt1 and Laata[i][1] != yt1 :
        xt3 = Laata[i][0]
        yt3 = Laata[i][1]
        i2 = i
        break

Lt3 = [0,i2]
for i in range(1,nunt1) :
    if i != i2  :
        xt2 = Laata[i][0]
        yt2 = Laata[i][1]
        Lt3.append(i)
        break
for i in range(1,nunt1) :
    if i not in Lt3  :
        xt4 = Laata[i][0]
        yt4 = Laata[i][1]
        Lt3.append(i)
        break

if xt1==xt2 :
    if yt2==yt3 and xt4==xt3 and yt4==yt1 :
        print('yes')
        sys.exit()
    else :
        print('no')
        sys.exit()
elif xt1==xt4 :
    if yt4==yt3 and xt2==xt3 and yt2==yt1 :
        print('yes')
        sys.exit()
    else :
        print('no')
        sys.exit()
