# class person:
#     count=0
    
#     def __init__(self,pname="",mobile=""):
#         print("in person coustructor")
#         person.count=person.count+1
#         self.__pid=person.count
#         self.__pname=pname
#         self.__mobile=mobile
        
#     @staticmethod
#     def myfunction(val,v):
#         print("in myfuction1",val,v,person.count)
        
#      #returns string for printing   
#     def __str__(self):
#         print("in person str method")
#         return f"pid:{self.__pid} Name:{self.__pname} Mobile:{self.__mobile}"
    
#     #setter methods
#     # def set_pid(self, pid ):
#     #     self.__pid=pid
        
#     def set_pname(self, pname ):
#         self.__panme=pname
        
#     def set_mobile(self, mobile ):
#         self.__mobile=mobile 
        
#     #gettter methods  
#     def get_pid(self):
#         return self.__pid
        
#     def get_pname(self):
#         return self.__pname
        
#     def get_mobile(self):
#         return self.__mobile
 
    
# if __name__=="__main__":
#     p1=person("Rajan","223333333333")
#     p2=person("Atharva","24563456345633")
    
#     print(p1)
#     print(p2)
    
#     print(p1.get_pname())
    
#     #to modify only mobile
#     p1.set_mobile(555555)
#     print(p1)

from abc import ABC, abstractmethod

class person:
    count=0
    
    def __init__(self,etype="",name="",mobile=""):

        person.count=person.count+1
        self.__id=etype+str(person.count)
        self.__name=name
        self.__mobile=mobile
        
    @staticmethod
    def myfunction(val,v):
        print("in myfuction1",val,v,person.count)
        
      #returns string for printing   
    def __str__(self):
       
        return f"id:{self.__id} Name:{self.__name} Mobile:{self.__mobile} "
    
    #setter methods
    # def set_id(self, id ):
    #     self.__id=id
        
    def set_name(self, name ):
        self.__anme=name
        
    def set_mobile(self, mobile ):
        self.__mobile=mobile 
        
    #gettter methods  
    def get_id(self):
        return self.__id
        
    def get_name(self):
        return self.__name
        
    def get_mobile(self):
        return self.__mobile
 
class employee(person, ABC):
    def __init__(self, etype="",name="",mob="",dt="",ds=""):
        super().__init__(etype,name,mob)
        self.__dept=dt
        self.__desg=ds
    @abstractmethod    
    def calculatesal():
        pass
        
    #setter method   
    def set_dept(self,dp):
        self.__dept=dp
    def set_desg(self,ds):
        self.__desg=ds
        
    #getter method   
    def get_dept(self,dp):
        return self.__dept
    
    def get_desg(self,ds):
        return self.__desg
        
        
    
    def __str__(self):
        return super().__str__()+ f"dept: {self.__dept} desg: {self.__desg} "


class salariedemp(employee):
    def __init__(self, name="",mob="",dt="",ds="",sal=1000):
        super().__init__("s",name,mob,dt,ds)
        self.__sal=sal
        self.__bonus=int(0.10*sal)
        
    #function overriding    
    def calculatesal(self):
        return self.__sal+.10*self.__sal+0.12*self.__sal
        
                
    #setter method   
    def set_sal(self,sal):
        self.__sal=sal
    def set_bonus(self,bonus):
        self.__bonus=bonus
        
    #getter method   
    def get_sal(self,sal):
        return self.__sal
    
    def get_bonus(self,bonus):
        return self.__bonus
        
        
    
    def __str__(self):
        return super().__str__()+ f"sal: {self.__sal} bonus: {self.__bonus}"
    


class contractdemp(employee):
    def __init__(self, name="",mob="",dt="",ds="",charges=1000,hrs=0):
        super().__init__("c",name,mob,dt,ds)
        self.__charges=charges
        self.__hrs=hrs
        
    #function overriding    
    def calculatesal(self):
        return self.__hrs*self.__charges  

            
    #setter method   
    def set_charges(self,charges):
        self.__charges=charges
    def set_hrs(self,hrs):
        self.__hrs=hrs
        
    #getter method   
    def get_charges(self,charges):
        return self.__charges
    
    def get_hrs(self,hrs):
        return self.__hrs
        
        
    
    def __str__(self):
        return super().__str__()+ f"charges: {self.__charges} hrs: {self.__hrs}"


if __name__=="__main__":
    s=salariedemp("Kishori","22222","UX","Mgr",77777)
    print(s)
    
    c=contractdemp("Rajesh","233333","game","Mgr",80000,30)
    print(c)

print(c.calculatesal())
print(s.calculatesal())













