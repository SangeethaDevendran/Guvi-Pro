cha,cho=map(int,input().split())
lists=list(map(int,input().split()))[:cha]
raa=int(input())
saa=(sum(lists)-lists[cho])//2
if (saa==raa):
    print("Bon Appetit")
else:
    print(abs(saa-raa))
