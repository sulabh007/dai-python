#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 09:06:28 2023

@author: dai
"""

print("""
a. display characters from even position
b. display characters from odd position
c. display length of a string
d. add a at the end of string length times
e. exit
""")

choice=""
while(choice!="e"):
    choice= str(input("Enter your choice: "))
    match choice:
        case "e":
            print("Program ended")
            break        
        case "a":
            str1= str(input("Enter a String: "))
            print(str1[::2])
        case "b":
            str1= str(input("Enter a String: "))
            print(str1[1::2])
        case "c":
            str1= str(input("Enter a String: "))
            print(len(str1))
        case "d":
            str1= str(input("Enter a String: "))
            print(str1+("a"*len(str1)))
        case other:
            print("Enter valid choice")


