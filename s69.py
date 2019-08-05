bob,sob=map(str,input().split("|"))
cot=input()
if  len(bob)>len(sob):
    if len(bob)==len(sob)+len(cot):
        print(bob+"|"+sob+cot)
elif len(bob)<len(sob):
     if len(sob)==len(bob)+len(cot):
        print(bob+cot+"|"+sob)
elif len(bob)==len(sob) and len(cot)>1 or (len(sob) or len(bob)):
    print("impossible")
