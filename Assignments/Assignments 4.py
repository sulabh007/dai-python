############################################Q1################################################

# import sys

# day=int(input("Enter number of days in month : "))
# if day>31 or day<28:
#     print("Invalid Input")
#     sys.exit()
# startday=int(input("Enter day the month begins on (0 for Monday, 1 for Tuesday, etc): "))
# if startday>6:
#     print("Invalid Input")
#     sys.exit()
# print("\n""M\tTu\tW\tTh\tF\tSa\tSu""\n")

# print(" \t"*startday,sep="",end="")
    
# for i in range(1,day+1):
#     print(i,end="\t")
#     if (i+startday)%7==0:
#         print("\n"*2)
    
############################################Q2################################################

# lst=input("Enter Numbers to create Histogram :")
# inp=[]
# lstlen=len(lst)
# for n in range(lstlen):
#     i=lst[n]
#     if i!=" ":
#         inp.append(int(i))       
# for el in inp:
#     print("*"*el)
    
############################################Q3################################################

# str=input("Enter a string for checking if its palindrome :")
# str=str.lower()
# str1=""
# strrev=""
# for i in str:
#     if i.isalpha()==True:
#         str1=str1+i
# strrev=str1[::-1]
# if str1==strrev:
#     print("This is a palindrome")
# else:
#     print("This is not a Palindrome")
    
############################################Q4################################################    


# str=input("Enter a string for checking if its a panagram :")
# str=str.lower()
# str1=""
# stra="qwertyuiopasdfghjklzxcvbnm"
# for i in str:
#     if i.isalpha()==True:
#         str1=str1+i
# for i in stra:
#     if str.find(i)==-1:
#         pan=False
#     else :
#         pan=True
# if pan==True:
#     print("This is a Panagram")
# else:
#     print("This is not a panagram")

############################################Q5################################################  

# str=input("Enter a string for translating it into robber's language :")

# def translate():
#     str1=""
#     check="aeiouAEIOU "
#     for i in str:
#         if check.find(i)==-1:
#             str1=str1+i+"o"+i
#         else:
#             str1=str1+i
#     return str1
 
# print(translate())

############################################Q6################################################  


# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# def main():
#     for i in range(1,21):
#         print(i,end=" : ")
#         print(factorial(i))   
        
# main()

############################################Q7################################################  

def add(n):
    if n==1:
        return 1
    else:
        return n+add(n-1)
          
def main():
    n=int(input("Enter a Number : "))
    print("Addition : ",add(n))
    
main()















