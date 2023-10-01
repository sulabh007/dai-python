# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:00:03 2023

@author: anilk
"""

from personclass import *
empdetails={}
#add new employee in the dictionary
def addnewemployee(ch):
    enm=input("enetr name")
    mob=input("enetr mobile")
    dt=input("enetr department")
    ds=input("enter desg")
    if ch==1:
        s=float(input("enter sal"))
        ob=SalariedEmp(enm,mob,dt,ds,s)
    else:
        hrs=int(input("enetr hrs"))
        charges=float(input("enetr charges"))
        ob=ContractEmp(enm,mob,dt,ds,charges,hrs)
    empdetails[ob.get_pid()]=ob

def displayall():
    for v in empdetails.values():
        print(v)

def deleteempbyid(eid):
    v=empdetails.get(eid,-1)
    if v!=-1:
        ch=input(f"do you want to delete {eid}")
        if ch=="y":
            empdetails.pop(eid)
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