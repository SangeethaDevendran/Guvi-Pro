import sys, string, math
sisa = input()
sisa = sisa.lower()
sont = string.ascii_lowercase

for c in sont :
    if c not in sisa :
        print('no')
        sys.exit()
print('yes')
