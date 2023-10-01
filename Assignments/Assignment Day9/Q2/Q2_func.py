from Q2_class import *

student_details = {}
ob= student("Kishor",45,45,54)
student_details[ob.get_sid()] = ob
ob1= student("Ramesh",77,77,77)
student_details[ob1.get_sid()] = ob1




def displayall():
    for student in student_details:
        print(student_details[student])


def addnewstudent(name, m1, m2, m3):
    ob = student(name, m1, m2, m3)
    student_details[ob.get_sid()] = ob

    
def searchbyid(sid) :
    value=student_details.get(sid)
    if value:
        print(student_details[sid])
    else:
        print("Sid not found")

    
def searchbyname(name):
    for sname in student_details.values():
        if name==sname.get_name():
            return sname
    return -1
            
def getgpabyid(sid):
    value=student_details.get(sid)
    if value:
        print(f"GPA of sudent {sid} is :",value.gpa())
    else:
        print("Sid not found")
    
        
        
        
        
        
        
        
    
