# choice=int(input("Enter a Number :"))
# match choice:
#     case 1:
#         print("Choice is 1")
#     case 2:
#         print("Choice is 2")
#     case 3:
#          print("Choice is 3")
#     case _:
#         print("in default case")  
        
# colour=int(input("Enter a colour :"))
# match colour:
#     case 1:
#         print("Choice is 1")
#     case 2:
#         print("Choice is 2")
#     case 3:
#          print("Choice is 3")
#     case others:
#         print("in default case")  

# import sys
# courselst=[("DBDA",100),("DAI",40)]
# def addnewcourse():
#     cname=input("Enter course name :")
#     capacity=int(input("Enter capacity :"))
#     courselst.append((cname,capacity))
#     return True

# def displayall(lst=courselst):
#     for cname,capa in lst:
#         print(f"{cname}--->{capa}")
        
# def searchcourses(searchc):
#     lst=[]
#     for cname,capa in courselst:
#         if capa>searchc:
#             lst.append((cname,capa))
#     return lst
# def searchbycname(old):
#     for pos,c in enumerate(courselst): #[(0,("DBDA",100)),(1,("DAI",40)))
#         if c[0]==old:
#             return pos,c
#     else:
#         return -1,None
        
        
# def modifybycourseName(old,new):
#     pos,cdetails=searchbycname(old)
#     if pos!=-1:
#         ans=input(f"do you want to modify {old} with {new}")
#         if ans=="y":
#             courselst[pos]=(new,cdetails[1])
#             return 1
#         else:
#             return 2
#     else:
#         return 3
 
# def deletebycourseName(coursename):
#     pos,cdetails=searchbycname(coursename)
#     if pos!=-1:
#         ans=input(f"do you want to delete {coursename} y/n :")
#         if ans=="y":
#             courselst.pop(pos)
#             return 1
#         else:
#             return 2
#     else:
#         return 3

# def modifybycourseCapacity(coursename,coursecap):
#     pos,cdetails=searchbycname(coursename)
#     if pos!=-1:
#         ans=str(input(f"do you want to modify {courselst[pos][1]} with {coursecap} y/n"))
#         if ans=="y":
#             courselst[pos]=(cdetails[0],coursecap)
#             return 1
#         else:
#             return 2
#     else:
#         return 3
    
    
# choice=0
# while choice!=7:
#     choice = int(input("""
#     1. add new course
#     2. delete the course
#     3. modify course duration
#     4. modify course name
#     5. display all
#     6. display only courses with capacity > given capacity
#     7. exit
#     choice:"""))
#     if choice==1:
#         status=addnewcourse()
#         if status:
#             print("new course added successfully")
#     elif choice==2:
#         coursename=input("Enter course name for deletion :")
#         status=deletebycourseName(coursename)
#         if status==1:
#             print("found and deleted ")
#         elif status==2:
#             print("found and not deleted")
#         else:
#             print("not found")
#     elif choice==3:
#         coursename=input("Enter course name :")
#         coursecap=input("Ente new course capacity :")
#         status=modifybycourseCapacity(coursename,coursecap)
#         if status==1:
#             print("found and modification done")
#         elif status==2:
#             print("found and not modified")
#         else:
#             print("not found")
#     elif choice==4:
#         oldcourse=input("Enter old course name :")
#         newcourse=input("Ente new course name :")
#         status=modifybycourseName(oldcourse,newcourse)
#         if status==1:
#             print("found and modification done")
#         elif status==2:
#             print("found and not modified")
#         else:
#             print("not found")
#     elif choice==5:
#         displayall()
#     elif choice==6:
#         searchc=int(input("enetr capacity to search courses"))
#         lstc=searchcourses(searchc)
#         displayall(lstc)
#     elif choice==7:
#         print("Thank you for visiting....")
#        sys.exit(0)





# #convert string into set
# s=set("This is set")
# print(s)

# #convert the list into set
# s=set(["Python","Perl","Python","OS","Linux"])
# print(s)

# s={12,34,22,(34,56),"data"}
# print(s)

# #add data in the set
# s.add(300)
# print(s)
       
# #s.add{[1,2,3]}  #error      
# s.update([1,2,3])
# print(s)

# #delete the data randomly
# print(s.pop())

# s.remove(300)
# print(s)


s1={1,2,3,4}
s2={4,5,11,12,13}
print("union",s1.union(s2),s1|s2)
print("intersection",s1.intersection(s2),s1&s2)
print("difference",s1.difference(s2),s1-s2)
s1.difference_update(s2)
#s1=s1-s2
print(s1)
print("symmetric_difference",s1.symmetric_difference(s2),s1^s2)
s1.symmetric_difference_update(s2)
#s1=s1^s2
print(s1)
s1={1,2,3,4}
s2={1,2}
print("superset", s1.issuperset(s2),s1>s2)
print("subset", s1.issubset(s2),s1<s2)
print("dissjoint", s1.isdisjoint(s2))
s1={1,100,2,200,3}
for data in s1:
    print(data)


















