cha=input()
cho=[]
for i in cha:
  if i not in cho:
    cho.append(i)
  else:
    break  
print(len(cho))
