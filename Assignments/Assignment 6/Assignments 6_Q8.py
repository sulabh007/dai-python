lst=["dxz","axz","bat","rat","cat","pat","bbc","bbm","cbm"]

wrd=input("Enter a word :")

find=0

for i,j in reversed(list(enumerate(lst))):
    print(f"{i} - {j}",end=" ")
    find=j.find(wrd[1])
    print(f"- {find}")
    if find==1:
        lst.insert(i+1,wrd)
        break
    
if find==-1:
    lst.append(wrd)
      
print(lst)

