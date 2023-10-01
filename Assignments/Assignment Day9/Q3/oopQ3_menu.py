from Q3_func import *

choice = "-1"

while choice != "":
    choice=input("""
          1. Display All Friends
          2. Add new friend
          3. Search by id
          4. Search by name
          5. Display all friend with a particular hobby
          6.Exit
          Enter your choice : """)
          
    match choice:
        case "1":
            displayall()
        case "2":
            name = input("Enter friends name : ")
            lname = input("Enter friends last name : ")
            hobbiesstr = input("Enter friends hobbies seprated by space : ")
            hobbies=hobbiesstr.split(" ")
            mob = int(input("Enter friends Mob NO. : "))
            email = input("Enter friends Email : ")
            bdate = input("Enter friends Birth Date : ")
            address = input("Enter friends Address : ")

            addnewfriend(name,lname, hobbies, mob, email, bdate, address)
        case "3":
            fid = input("Enter friends id : ")
            searchbyid(fid)
        case "4":
            name = input("Enter friends name : ")
            fname=searchbyname(name)
            if fname !=-1:
                print(fname)
            else:
                print("Name not found")
        case "5":
            hobby = input("Enter Hobby: ")
            status=searchbyhobby(hobby)
            if status==-1:
                print("Hobby not found")
        case "6":
            print("Thank you for visiting")
            break
        case _:
            print("Invalid choice")
