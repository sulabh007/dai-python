
def delel(set1):
    el=int(input("Enter element to delete :"))
    set1.discard(el)
    
def  addel(set1):
    el=int(input("Enter element to add :"))
    set1.add(el)
    
def createset():
    set2=set()
    set2.add(int(input("Input set element :")))
    return set2

def setunion(set1,set2):
    print(set1.union(set2))
    return set1

def setintersection(set1,set2):
    print(set1.intersection(set2))
    return set1

def setdifference(set1,set2):
    print(set1.difference(set2))
    return set1

def settofrozenset(set1):
    frzset=frozenset(set1)
    return frzset
