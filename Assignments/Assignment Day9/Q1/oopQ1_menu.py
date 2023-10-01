from Q1_func import *

choice = "-1"

while choice != "":
    choice=input("""
          a. Display all students
          b. Add new student
          Enter your choice : """)
          
    match choice:
        case "a":
            displayall()
        case "b":
            name = input("Enter students name : ")
            m1 = input("Enter students M1 marks : ")
            m2 = input("Enter students M2 marks: ")
            m3 = input("Enter students M3 marks: ")
            addnewstudent(name, m1, m2, m3)
        case "c":
            pass
        case 4:
            pass
        case 5:
            pass
        case "a":
            pass
        case "a":
            pass
        case _:
            pass
