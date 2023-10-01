#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 17:08:58 2023

@author: dai
"""
################################Q1#############################################

# str1=str(input("Enter odd number string greater than 7 :"))
# strlen=len(str1)
# mid=(strlen//2)-1
# print(str1[mid:mid+3])

################################Q2#############################################


# str1=str(input("Enter a string 1:"))
# str2=str(input("Enter a string 2:"))
# strlen=len(str1)
# mid=int(strlen//2)
# print(str1[:mid]+str2+str1[mid:])

################################Q3###########################################

# str1=str(input("Enter a string 1:"))
# str2=str(input("Enter a string 2:"))
# strlen1=len(str1)
# strlen2=len(str2)
# mid1=int(strlen1//2)
# mid2=(int(strlen2//2))

# print(str1[0]+str2[0]+str1[mid1]+str2[mid2]+str1[-1]+str2[-1])

################################Q4###########################################

# str1=str(input("Enter a string :"))
# upper=""
# lower=""
# for a in str1:
#     if a.isupper()==True:
#         upper=upper+a
#     if a.islower()==True:
#         lower=lower+a
# print(upper+lower)
        
 ################################Q5###########################################   

str1=str(input("Enter a string 1:"))
str2=str(input("Enter a string 2:"))
strlen1=len(str1)
strlen2=len(str2)
substr=""
str2rev=str2[::-1]
if strlen2>strlen1:
    cnt=strlen2-strlen1
    substr=str2rev[cnt:]
if strlen2<strlen1:
    cnt=strlen1-strlen2    
    substr=str1[cnt:]
str3=""


for i in range(min(strlen1,strlen2)):
    str3=str3+str1[i]+str2rev[i]
str3=str3+substr
    
    
print(str3)
        











