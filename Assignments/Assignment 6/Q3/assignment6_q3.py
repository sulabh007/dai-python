from function_q3 import *
lst = [13,55,66,77,11,12,13,14,15,16]


choice = 0
print("""
               1. Accept Data
                   a) add at last position
                   b) add at given position
               2. Delete data by value display message deleted successfully or not found
               3. delete data by position
                   a) delete last element
                   b) delete from particular position
               4. sort
                   a) ascending
                   b) descending
               5. reverse
               6. Print in sorted order without changing original list
               7. print in reverse order without changing original list
               8. display data
                   a) normal
                   b) numbered""")

choice = int(input("Enter your choice : "))
match choice:
    case 1:
        lst = acceptdata(lst)
        print(lst)
    case 2:
        lst = deletedatabyvalue(lst)
        print(lst)
    case 3:
        lst = deletedatabypos(lst)
        print(lst)
    case 4:
        lst = sort(lst)
        print(lst)
    case 5:
        lst = reverse(lst)
        print(lst)
    case 6:
        lst1 = sortcopy(lst)
        print(lst)
        print(lst1)
    case 7:
        lst1 = revsortcopy(lst)
        print(lst)
        print(lst1)
    case 8:
        lst = displaydata(lst)
    case 9:
        print("Thank you for using our program.")
    case _:
        print("Invalid Choice")
