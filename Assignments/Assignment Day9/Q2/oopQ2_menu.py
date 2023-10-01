from Q2_func import *

choice = "-1"

while choice != "":
    choice=input("""
          a. Display all students
          b. Add new student
          c. Search by id
          d. Search by name
          e. Calculate GPA of a student
          f.Exit
          Enter your choice : """)
          
    match choice:
        case "a":
            displayall()
        case "b":
            name = input("Enter students name : ")
            m1 = int(input("Enter students M1 marks : "))
            m2 = int(input("Enter students M2 marks: "))
            m3 = int(input("Enter students M3 marks: "))
            addnewstudent(name, m1, m2, m3)
        case "c":
            sid = input("Enter students id : ")
            searchbyid(sid)
        case "d":
            name = input("Enter students name : ")
            sname=searchbyname(name)
            if sname !=-1:
                print(sname)
            else:
                print("Name not found")
        case "e":
            sid = input("Enter students id : ")
            getgpabyid(sid)
        case "F":
            print("Thank you for visiting")
            break
        case _:
            print("Invalid choice")
