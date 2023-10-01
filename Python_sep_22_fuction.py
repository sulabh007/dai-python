from Python_sep_22 import *
empdetails=[]
empdetails=[["s1","Kishori",23452345,"Game","mgr",12431243],["c2","Kishori",23452345,"UX","mgr",77,345345]]
#add new employee in the dictionary
def addnewemployee(ch):
    enm=input("Enter name")
    mob=input("Enter mobile")
    dt=input("Enter department")
    ds=input("Enter desg")
    if ch==1:
        s=float(input("Enter sal"))
        ob=SalariedEmp(enm,mob,dt,ds,s)
    else:
        hrs=int(input("Enter hrs"))
        charges=float(input("Enter charges"))
        ob=ContractEmp(enm,mob,dt,ds,charges,hrs)
    empdetails[ob.get_pid()]=ob

def displayall():
    
    for v in empdetails:
        print(v)

def deleteempbyid(eid):
    empdetails=[["s1","Kishori",23452345,"Game","mgr",12431243],["c2","Kishori",23452345,"UX","mgr",77,345345]]
    eid="c2"
    for i in range(len(empdetails)):
        pos=empdetails[i].index(eid)
    if pos!=-1:
        ch=input(f"do you want to delete {eid} y/n :")
        if ch=="y":
            empdetails.pop(pos)
            return 1
        else:
            return 2
    else:
        return 3
    
def modifydetails(eid,s=0,ch=1):
    v=empdetails.get(eid,-1)
    if v!=-1:
        if isinstance(v,SalariedEmp):
            v.set_sal(s)
        elif isinstatnce(v,ContractEmp):
            v.set_hrs(s)
            v.set_charges(ch)
            
def getCalculatedNetSal(eid):
    v=empdetails.get(eid,-1)
    if v!=-1:
        #dynamic polymorophism
        return v.calculatesal()
    else:
        return -1

def findByType(ch):
    lst=[]
    if ch==1:
        for v in empdetails.values():
            if isinstance(v,SalariedEmp):
                lst.append(v)
    else:
        for v in empdetails.values():
            if isinstance(v,ContractEmp):
                lst.append(v)
    if lst:
        return lst
    else:
        return None
            
def findBySalary(sal):    
    lst=[]
    for v in empdetails.values():
        if isinstance(v,SalariedEmp):
            if v.get_sal()>sal:
                lst.append(v)
        else:
            if v.get_charges()>sal:
                lst.append(v)
    if lst:
        return lst
    else:
        return None

