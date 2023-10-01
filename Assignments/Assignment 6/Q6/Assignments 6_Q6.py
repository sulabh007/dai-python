from funcq6 import *
set1={1,2,3,4,5,6,7,8,9}

choice=0
print("""1. delete element if exists otherwise
do not show any errr""")
print("2. add a elemet")
print("3. create one more set")
print("4. union of 2 sets")
print("5. intersection of 2 sets")
print("6. difference of 2 sets")
print("7. convert set into frozenset")
print("8. exit")
while choice!= 8:
    choice=int(input("Enter your choice :"))
    
    match choice:
        case 1:
            delel(set1)
        case 2:
            addel(set1)
        case 3:
            set2=set(createset())
        case 4:
            setunion(set1,set2)
        case 5:
            setintersection(set1,set2)
        case 6:
            setdifference(set1,set2)
        case 7:
            frznset = settofrozenset(set1)
        case 8:
            print("Thank you for using our programe")
        case _:
            print("Invalid choice")

