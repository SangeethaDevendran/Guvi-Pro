import sys, string, math
cha = int(input())
che = [ int(x) for x in input().split()]
sha = []
duplicate = []
she = []
for i in range(1,cha+1) :
    if i not in che:
        sha.append(i)
for i in che :
    if che.count(i) > 1 and i not in duplicate :
        duplicate.append(i)
for i in range(0,cha) :
    if che[i] in duplicate :
        she.append(i)
cho = len(sha)
for i in range(0,cha) :
    if len(sha) == 0 :
        break
    if i in she :
        if i == she[0] :
            if sha[0] < che[i] :
                che[i] = sha.pop(0)
                she.pop(0)
            elif che[i] in duplicate :
                she.pop(0)
                duplicate.remove(che[i])
            else :
                che[i] = sha.pop(0)
                she.pop(0)


print(cho)
print(*che)
