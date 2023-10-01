from Assignment_Day11_Q1_Func import *
 
    
choice = 0  
    
while choice != 7:
    choice=int(input(""" 
        1.Add Employee
        2.Delete Employee
        3.Modify Employee
        4.Display all Employees 
        5.Display Employee based on empid 
        6.Display all Employee with Sal > given Sal
        7.Exit
        Enter Choice : """))
    match choice:
        case 1:
            empid=int(input("Enter Employee ID :"))
            empname=input("Enter Employee Name :")
            mob=int(input("Enter Mob No. :"))
            sal=float(input("Enter Employee Salary :"))
            addemp(empid,empname,mob,sal)
        case 2:
            empid=int(input('Enter employee ID to delete employee :'))
            status=delemp(empid)
            if status==1:
                print("Succesfully Deleted")
            else:
                print(f"No employee with empid: {empid}")
        case 3:
            empid=int(input('Enter employee ID to modify employee :'))
            empname=input("Enter Employee Name :")
            mob=int(input("Enter Mob No. :"))
            sal=float(input("Enter Employee Salary :"))
            status=modemp(empid,empname,mob,sal)
            if status==1:
                print("Succesfully Modified")
            else:
                print(f"No employee with empid: {empid}")
        case 4:
            displayempall()
        case 5:
            empid=int(input('Enter employee ID :'))
            displybyid(empid)
        case 6:
            sal=float(input("Enter Employee Salary :"))
            displaybysal(sal)
        case 7:
            print("Thank you for visiting.....")
        case _:
            print("Invalid Input")
