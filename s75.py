cha,cho=map(int,input().split())
Lists=list(map(int,input().split()))[:cha]
rtd=int(input())
Soop=(sum(Lists)-Lists[cho])//2
if (Soop==rtd):
    print("Bon Appetit")
else:
    print(abs(Soop-rtd))
