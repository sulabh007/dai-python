from Q1_class import *

student_details = {}


def displayall():
    for student in student_details:
        print(student_details[student])


def addnewstudent(name, m1, m2, m3):
    ob = student(name, m1, m2, m3)
    student_details[ob.get_pid()] = ob
