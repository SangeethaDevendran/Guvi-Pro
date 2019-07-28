import sys, string, math
sha = input()
if sha == sha[::-1] :
    print('yes')
    sos.exit()
cha = 0
for case in sha[::-1] :
    if case == '0' :
         cha += 1
    else :
        break
sopa = '0'*cha + sha
if sopa == sopa[::-1] :
    print('yes')
else :
    print('no')
