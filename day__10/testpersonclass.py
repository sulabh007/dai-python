# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:02:03 2023

@author: anilk
"""

from personservice import *
            
choice=0
while choice!=8:
    choice=int(input("""
          1. add new employee
          2. delete the employee by id
          3. modify sal or charges
          4. display all
          5. calculate net sal by id
          6. display only given type of employee
          7. display all with sal>given value
          8. exit
          """))
    match choice:
        case 1:
            ch=int(input("1. Salaried 2. Contract" ))
            addnewemployee(ch)
        case 2:
            eid=input("enter eid")
            status=deleteempbyid(eid)
            if status==1:
                print("deleted successfully")
            elif status==2:
                print("deleted but not found")
            else:
                print("not found")
        case 3:
            eid=input("enter eid")
            if eid.startswith("s"):
                s=float(input("enetr salary"))
                status=modifydetails(eid,s)
            else:
                hrs=int(input("enetr hrs"))
                charges=float(input("enetr charges"))
                status=modifydetails(eid,hrs,charges)
                
        case 4:
            displayall()
        case 5:
            eid=input("enter eid")
            netsal=getCalculatedNetSal(eid)
            if netsal!=-1:
                print(f"Employee Id: {eid},Net Salary :{netsal}  ")
            else:
                print("not found")
        case 6:
            ch=int(input("1. Salaried 2. Contract" ))
            lst=findByType(ch)
            if lst!=None:
                for v in lst:
                    print(v)
            else:
                print("not found")
        
        case 7:
            sal=float(input("enter salary"))
            lst=findBySalary(sal)
            if lst!=None:
                for v in lst:
                    print(v)
            else:
                print("not found")
        case 8:
            print("Thank you for visiting......!!")
        case _:
            print("wrong choice")
            
            
            
            
            
            