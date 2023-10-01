# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Mon Sep 18 10:05:58 2023

# @author: dai
# """
# d={"DBDA":(100,60),"DAI":(200,50)}
# print("length",len(d))
# print(d)

# #to add a new key value pair in the dictionary
# #if key not there it will add,
# #otherwise it will overwrite
# d["DAC"]=(230,240)
# print("length",len(d))
# print(d)

# d1={(1,2):"xxxx",(3,4):"ttt"}
# print(d1[(1,2)])
# print(d1)

# #to check whether key exitsts
# v=d.get("DBDA")
# if v==None:
#     print("Not Found")
# else:
#     print("key found and value :",v)
# print(d)


# v=d.get("DBDA1")
# if v==None:
#     print("Not Found")
# else:
#     print("key found and value :",v)
# print(d)

# v=d.get("DBDA1",-1)
# if v==-1:
#     print("Not Found")
# else:
#     print("key found and value :",v)
# print(d)

# v=d.setdefault("DBDA1",-1)
# if v==-1:
#     print("Not Found")
# else:
#     print("key found and value :",v)
# print(d)

# #to navigate through all keys and values
# for k in d.keys():
#     print(f"{k}------->{d[k]}")
# for k,v in d.items():
#     print(f"{k}------->{v}")
# #or to  search keys based on values
# for k in d.keys():
#     if d[k][1]>50:
#         print(f"{k}------->{d[k]}")
# for k,v in d.items():
#     if d[k][1]>50:
#         print(f"{k}------->{v}")

# print(d.values())


# v=d.pop("DBDA")
# print(v,d)

# v=d.pop("DBDA",-1)
# if v==-1:
#         print("not found")
# else:
#         print("not found")
#         print(v,d)

# data=d.popitem()
# print(data)

# d={"DBDA":(100,60),"DAI":(200,50)}
# lst=[11,12,13]
# d3=dict.fromkeys(lst);
# print(d)
# d4=dict.fromkeys(lst,1000)
# print(d4)

# d1={"a":10,"b":20}
# d2={"a":25,"c":30}
# d1.update(d2)
# print(d1)


# course={"DBDA":(100,60),"DAI":(200,50)}
# def addnewcourse():
#     cname=input("Enter course name :")
#     duration=int(input("Enter course durantion :"))
#     capacity=int(input("Enter course capacity :"))
#     #value=course.setdefault(cname,(duration,capacity))
#     value=course.get(cname,-1)
#     if value==-1:
#         course[cname]=(duration,capacity)
#         return True
#     else:
#         return False

# def displayall(d=course):
#     for k,v in d.items():
#         print(f"{k}--->{v}")
        
# def displaybycapacity(capacity):
#     d={}
#     for k,v in course.items():
#         if v[1]>capacity:
#           d[k]=v
#     if len(d)!=0:
#         return d
#     return None

# def delclource():
#     cname=input("Enter course name : ")
#     value=course.get(cname,-1)
#     if value!=-1:
#         course.pop(cname)
#         return True
#     else:
#         return False

# def modcoursecap():
#     cname=input("Enter course name : ")
#     duration=course[cname][0]
#     capacity=int(input("Enter new course capacity : "))
#     value=course.get(cname,-1)
#     if value!=-1:
#         course[cname]=(duration,capacity)
#         return True
#     else:
#         return False
# def modcoursename():
#     cname=input("Enter course name : ")
#     duration,capacity=course[cname]
#     newcname=(input("Enter new course name : "))
#     value=course.get(cname,-1)
#     if value!=-1:
#         course.pop(cname)
#         course[newcname]=(duration,capacity)
#         return True
#     else:
#         return False
    
# def modcoursedur():
#     cname=input("Enter course name : ")
#     capacity=course[cname][1]
#     duration=int(input("Enter new course duration : "))
#     value=course.get(cname,-1)
#     if value!=-1:
#         course[cname]=(duration,capacity)
#         return True
#     else:
#         return False      
    

# choice=0
# while choice!=7:
#     choice = int(input("""
#     1. add new course
#     2. delete the course
#     3. modify course capacity
#     4. modify course duration
#     5. modify course name
#     6. display all
#     7. display only courses with capacity > given capacity
#     8. exit
#     choice: """))
#     match choice:
#         case 1:
#             status=addnewcourse()
#             if status:
#                 print("course added")
#             else:
#                 print("course exists")
#         case 2:
#             status=delclource()
#             if status:
#                 print("Course Deleted")
#             else:
#                 print("Course not Deleted")
#         case 3:
#             status=modcoursecap()
#             if status:
#                 print("Course Capacity modified")
#             else:
#                 print("Course Capacity  not modified")
#         case 4:
#             status=modcoursedur()
#             if status:
#                 print("Course duration modified")
#             else:
#                 print("Course duration not modified")
#         case 5:
#             status=modcoursename()
#             if status:
#                 print("Course name modified")
#             else:
#                 print("Course name  not modified")
#         case 6:
#            displayall()
#         case 7:
#             capacity=int(input("Enter capacity"))
#             data=displaybycapacity(capacity)
#             if data!=None:
#                 displayall(data)
#             else:
#                 print("No course found")
#         case 8:
#             print("Thank you for visiting.....")
#         case _:
#             print("wrong choice")
        
    



# def f1(a=12,b=13,c=13,*tp,**kwarg):
#     print(a,b,c)
#     print(tp)
#     print(kwarg)
#     s=a+b+c
#     for d in tp:
#         s=s+d
#     for k in kwarg.values():
#         s=s+k
#     return s

# print("Sum ",f1(1,2,3))
# print("Sum ",f1(11,21,31,2,3,4,5,6,7,x=110,y=220,z=444))

def f1(""):
    print("in fuction f1")

def f2(""):
    print("in fuction f2")





























