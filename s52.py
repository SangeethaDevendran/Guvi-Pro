import sys,string
def maxOfSegmentMinimum(Lacs, necs, kins):
    if kins == 1:
        return min(Lacs)
    if kins == 2 :
        return max(Lacs[0], Lacs[necs - 1])
    return max(Lacs)

necs,kins = map(int,input().split())
Lacs = [ int(x) for x in input().split()]
necs = len(Lacs)
ans = maxOfSegmentMinimum(Lacs, necs, kins)
print(ans)
