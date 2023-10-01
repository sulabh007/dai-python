# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 10:09:20 2023

@author: anilk
"""
from abc import ABC,abstractmethod
class Person:
    count=0
    def __init__(self,etype="",pname="",mob=""):
        print("in person constructor")
        Person.count=Person.count+1
        self.__pid=etype+str(Person.count)
        self.__pname=pname
        self.__mobile=mob
        
    @staticmethod
    def myfunction1(val,v):
        print("in myfunction1",val,v,Person.count)
              
     #setter methods
    def set_pid(self,pid):
        self.__pid=pid
        
    def set_pname(self,pnm):
        self.__pname=pnm 
        
    def set_mobile(self,mob):
        self.__mobile=mob
     
    #getter methods
    def get_pid(self):
        return self.__pid
    
    def get_pname(self):
        return self.__pname
    
    def get_mobile(self):
        return self.__mobile
        
    def __str__(self):
        print("In person str method")
        return f"Id: {self.__pid} Name: {self.__pname} Mobile:{self.__mobile}"

class Employee(Person,ABC):
    def __init__(self, etype="",pname="",mob="",dt="",ds=""):
        super().__init__(etype,pname,mob)
        self.__dept=dt
        self.__desg=ds
    #setter method
    def set_dept(self,dt):
        self.__dept=dt
    def set_desg(self,ds):
        self.__desg=ds 
        
    @abstractmethod
    def calculatesal(self):
        pass
    
    #getter method
    def get_dept(self):
         return self.__dept
    def get_desg(self):
         return self.__desg    
        
    def __str__(self):
        return super().__str__()+f"dept: {self.__dept} desg: {self.__desg}"
    
class SalariedEmp(Employee):
    def __init__(self,pname="",mob="",dt="",ds="",sal=1000):
        super().__init__("s",pname,mob,dt,ds)
        self.__sal=sal
        self.__bonus=0.10*sal
    #setter methods
    def set_sal(self,s):
        self.__sal=s
    def set_bonus(self,b):
        self.__bonus=b 
     #getter method
    def get_sal(self):
         return self.__sal
    def get_bonus(self):
         return self.__bonus
    def __str__(self):
         return super().__str__()+f"sal: {self.__sal} bonus: {self.__bonus}"
    #function overriding 
    def calculatesal(self):
        return self.__sal+.10*self.__sal+0.12*self.__sal-0.08*self.__sal+self.__bonus
    def calculatebonus(self,percent):
        return (percent/100)*self.__sal
        
        
class ContractEmp(Employee):
    def __init__(self,pname="",mob="",dt="",ds="",charges=1000,hrs=0):
        super().__init__("c",pname,mob,dt,ds)
        self.__hrs=hrs
        self.__charges=charges
    #setter methods
    def set_hrs(self,s):
        self.__hrs=s
    def set_charges(self,c):
        self.__charges=c 
     #getter method
    def get_hrs(self):
         return self.__hrs
    def get_charges(self):
         return self.__charges
    def __str__(self):
         return super().__str__()+f"Charges: {self.__charges} hrs: {self.__hrs}" 
    def calculatesal(self): 
         return self.__charges*self.__hrs
        
if __name__=="__main__": 
    s=SalariedEmp("Kishori","2222","UX","Mgr",77777)
    print(s)
    print(s.calculatesal())
    c=ContractEmp("Raesh","3333","game","Mgr",8000,30)
    print(c)
    print(c.calculatesal())
'''       
    p1=Person("Rajan","22222")
    p2=Person("Atharva","3333")
    #to print all the member
    print(p1) 
    print(p2)
    
    #to retrieve only name
    print(p1.get_pname()) 
    
    #to modify only mobile
    p1.set_mobile(55555)
    print(p1)  
    Person.myfunction1(10,23)
            
'''        
        
        
        
    
    