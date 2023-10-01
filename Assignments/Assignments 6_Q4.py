lst1=[]
lst2=[]

el=""
while el!="q":
    el=str(input("""Enter cities or enter "q" to quit :"""))
    lst1.append(el)
el=""
while el!="q":
    el=str(input("""Enter location of cities or enter "q" to quit :"""))
    lst2.append(el)

for i,j  in zip(lst1,lst2):
    print(f"{i} - {j}")