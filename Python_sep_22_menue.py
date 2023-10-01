from Python_sep_22_fuction import *


empdetails=[]
empdetails=[["s1","Kishori",23452345,"Game","mgr",12431243],["c2","Kishori",23452345,"UX","mgr",77,345345]]

        
        
choice=0
while choice!=8 :
    
    match choice:
        case 1:
            ch=int(input("1. Salaried 2. Contract" ))
            addnewemployee(ch)
        case 2:
            eid=input("Enter eid")
            status=deleteempbyid(eid)
            if status==1:
                print("deleted successfully")
            elif status==2:
                print("deleted but not found")
            else:
                print("not found")
        case 3:
            eid=input("Enter eid")
            if eid.startswith("s"):
                s=float(input("Enter salary"))
                status=modifydetails(eid,s)
            else:
                hrs=int(input("Enter hrs"))
                charges=float(input("Enter charges"))
                status=modifydetails(eid,hrs,charges)
                
        case 4:
            displayall()
        case 5:
            eid=input("Enter eid")
            netsal=getCalculatedNetSal(eid)
            if netsal!=-1:
                print(f"Employee Id: {eid},Net Salary :{netsal}  ")
            else:
                print("Not found")
        case 6:
            ch=int(input("1. Salaried 2. Contract" ))
            lst=findByType(ch)
            if lst!=None:
                for v in lst:
                    print(v)
            else:
                print("Not found")
        
        case 7:
            sal=float(input("Enter salary"))
            lst=findBySalary(sal)
            if lst!=None:
                for v in lst:
                    print(v)
            else:
                print("Not found")
        case 8:
            print("Thank you for visiting......!!")
        case _:
            print("Wrong choice")
            