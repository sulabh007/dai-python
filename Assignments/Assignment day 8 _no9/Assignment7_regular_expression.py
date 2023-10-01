######################################Q1####################################
import re
# regex="\w+\@"

# email=str(input("Enter Email : "))

# name=re.match(regex, email, re.I)

# str1=name.group().strip("@")
# if name!=None:
#     print(str1)
# else:
#     print("Not found")

    
######################################Q2####################################


# line=input("Enter Line :")

# num=re.match( "\d|^\D[a-zA-Z]{1,}" , line, re.I)

# if num!=None:
#     print(line)
# else:
#     print("Line does not match")
    
    
######################################Q3####################################

# regex="^\d{10}"

# mob=input("Enter Mobile Number :")

# num=re.match( regex ,mob, re.I)

# if num!=None:
#     print(f"{mob} is a valid mobile number")
# else:
#     print("Invalid Mobile Number")
    

######################################Q4####################################

usrnregex="\w+"
pswregex="^(?=[a-zA-Z])(?=.*[^a-zA-Z0-9]).{8,}$"

usn=input("Enter Username :")

usrnc=re.match( usrnregex ,usn, re.I)

if usrnc:
    print("Username is valid")
else:
    print("Username is not valid")
    usn=input("Enter valid Username :")
    
psw=input("Enter Password :")

pswc=re.match( pswregex ,psw)   

attempt=3

while attempt!=0 :
    if pswc:
        print("Welcome to our application")
        break
    else:
        attempt=attempt-1
        print("Password length should be 8 starts with alphabet and should contain at least one special character")
        print(f"{attempt} attempt remaining")
        psw=input("Enter valid Password :")
        pswc=re.match( pswregex ,psw)
        
if attempt==0:
    print("No remaining attempts")
        
    






















