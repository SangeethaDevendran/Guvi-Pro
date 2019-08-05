cha=int(input())
cho,che=3,3
lists=[]
lists.append(3)
for i in range(1,cha+1):
    if cho==1:
        cho=2*che
        che=cho
        lists.append(cho)
    else:
        cho=cho-1
        lists.append(cho)
print(lists[cha-1])
