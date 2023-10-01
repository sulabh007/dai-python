
def acceptdata(lst):
    choice=input(("""
    a) add at last position
    b) add at given position 
    Enter Choice :"""))
    if choice == "a":
        el=int(input("Enter data to add :"))
        lst.append(el)
        return lst
    elif choice == "b":
        pos = int(input("Enter position to add :"))
        el = int(input("Enter data to add :"))
        lst.insert(pos,el)
        return lst
    else:
        print("Invalid choice")

def deletedatabyvalue(lst):
    el=int(input("Enter data to delete :"))
    ind=lst.index(el)
    if ind >= 0:
        ans=input("Are you sure Y/N :")
        if ans == "y" or "Y":
            lst.remove(el)
            return lst
            print("Value removed")
        elif ans == "n" or "N":
            print("Value not removed")
        else:
            print("Invalid input")
    else:
        print("Value not found")
    
def deletedatabypos(lst):
    choice=input(("""
    a) delete last element
    b) delete from particular position
    Enter Choice :"""))
    if choice == "a":
        lst.pop()
        return lst
    elif choice == "b":
        pos = int(input("Enter position to delete :"))
        lst.pop(pos)
        return lst
    else:
        print("Invalid choice")
        
def sort(lst):
    choice=input(("""
    a) ascending
    b) descending
    Enter Choice :"""))
    if choice == "a":
        lst.sort()
        return lst
    elif choice == "b":
        lst.sort(reverse=True)
        return lst
    else:
        print("Invalid choice")
        
def reverse(lst):
        lst.reverse()  
        return lst
    
def sortcopy(lst):
    lst1=sorted(lst)
    return lst1
    
def revsortcopy(lst):
    lst1=list(reversed(lst))
    return lst1

def displaydata(lst):
    lst = [13, 55, 66, 77, 11, 12, 13, 14, 15, 16]
    choice=input(("""
    a) normal
    b) numbered
    Enter Choice :"""))
    if choice == "a":
        for i,el in enumerate(lst):
            print(f"{el}",end=" ")
    elif choice == "b":
        for i,el in enumerate(lst):
            print(f"{i} - {el}")
    else:
        print("Invalid choice")
    
    
    
    
