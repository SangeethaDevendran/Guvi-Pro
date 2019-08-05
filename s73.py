cha=input()
chi=[]
for p in cha:
  if p not in chi:
    chi.append(p)
  else:
    break  
print(len(chi))
