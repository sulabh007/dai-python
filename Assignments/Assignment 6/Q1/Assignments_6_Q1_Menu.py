from q1function import displayeven, displayodd, lenstr, adda

choice = ""

str1 = str(input("Enter a String: "))

while choice != "e":
    choice = input("""
    a. display characters from even position
    b. display characters from odd position
    c. display length of a string
    d. add a at the end of string length times
    e. exit
    Enter your choice : """)
    match choice:
        case "a":
            displayeven(str1)
        case "b":
            displayodd(str1)
        case "c":
            lenstr(str1)
        case "d":
            adda(str1)
        case "e":
            print("Thank you for using our program.")
        case _:
            print("Invalid Input")
