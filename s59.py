cha=input()
cho=input()
che=cha.index('|')
doa=len(cha)+len(cho)
if doa%2==0:
    print("Impossible")
else:
    if che<=doa//2-1:
        cha=cho+cha
    else:
        cha=cha+cho
    che=cha.index('|')
    if che!=doa//2-1 and che!=doa//2:
        print("Impossible")
    else:
        print(cha)
