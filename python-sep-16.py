#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 09:10:01 2023

@author: dai
"""

# lst=[10,20,10,34]
# lst.append("Hello")
# print(len(lst))
# print(lst)
# lst.extend("Testing")
# print(len(lst))
# print(lst)

# lst=[10,20,10,34]
# lst.append([1,2,3])
# print(len(lst))
# print(lst)
# lst.extend([12,13,22,22])
# print(len(lst))
# print(lst)

# #delet the element from the end
# lst.pop()
# print(lst)

# #to delete the element from the given position
# lst.pop(2)
# print(lst)
# #to delete the given value from the list
# lst.remove(10)
# print(lst)
# #it will throw an exception
# if (100 in lst ):
#     lst.remove(100)
# else:
#     print("not found")
# print(lst)

# #index function will find the positon
# #if found otherwise throw exception
# print("index of 34",lst.index(34))

#lst.index(100) #throws exception
    
# lst=[1,2,3,4,5,6,3,4]
# lst.sort()
# print(lst)

# lst.sort(reverse=True)
# print(lst)

# lst.reverse()    
# print(lst)
    
# lst=[12,23,34]

# #it will copy the referance
# #changes in one list eill be reflected in anaother list
# lst1=lst

# lst.append(100)
# print(lst)
# print(lst1)

# #create a shallow copy of the list
# lst2=lst.copy()
# lst.append(200)
# print(lst,lst1)
# print(lst2)



# import copy

# lst=[10,20,30,[1,2,3]]
# lst1=copy.deepcopy(lst)
# lst[3].append(100)
# print(lst,lst1)

# lst=[10,20,30,[1,2,3]]
# lst1=copy.copy(lst)
# lst[3].append(100)
# print(lst,lst1)


# lst=[12,1,23]
# lst1=["Pune","mumbai","delhi","Kolkatta"]

# #to read data simulteneously from multiple lists
# for val in zip(lst,lst1):
#     print(val[0],"------->"val[1])
    
# for x,y in zip(lst,lst1):
#     print(x,"----->",y)

# lst=["a","b","c"]
# cnt=0
# for i in lst:
#     print(cnt,"---->",i)
    
    
    
    
    
    
    
# lst=[12,1,3,23,12,25]
# #to find all even numbers

# lst1=[]
# for num in lst:
#     if num%2==0:
#         lst1.append(num)

# print(lst1)

# lst1=[num for num in lst if num%2==0]
# print(lst1)

# #lambda function
# print(lst)
# lst2=list(filter(lambda x:x%2==0 and x>10 ,lst))
# print(lst2)

# def f1(n):
#     n=n+10
#     return n%2==0 and n>15

# lst2=list(filter(lambda x:f1(x),lst))
# print(lst2)

# lst=[1,2,12,13,10]
# lst1=[]
# for num in lst:
#     lst1.append(num+10)
# print(lst1)


# lst1=[num+10 for num in lst]

# print(map(lambda x:x+10 ,lst))

# lst1=list(map(lambda x:x+10 ,lst))

# print(lst1)

import functools

# lst=[1,2,12,13,10]
# s=functools.reduce(lambda acc,num:acc+num, lst)
# print("additon", s)
# print("addition", sum(lst))

# lst=["Python","perl","linux","os"]
# s=functools.reduce(lambda acc,num:acc+num, lst)
# print("additon", s)
##
##lst=["Python","perl","linux","os"]
##s=functools.reduce(lambda acc,s:acc if len (acc)>len(s) else s ,lst)
##
###write a fuction to find a string generated by cocataion 2 and 3rd character of every string
##
##s=functools.reduce(lambda acc,s:acc+s[1:3] ,lst,"")
##
##print("string", s)
##
##
##lst=[(1,"zzz",45),(0,"bbb",56),(5,"aaa",46)]
##s=lst.sort(key=lambda x:x[1])
##print(lst)




##num=int(input("Enter a Number : "))
##
##def factorial(num):
##    if num==1:
##        return 1
##    else:
##        return num*factorial(num-1)
##print(factorial(num))

##num=int(input("Enter a Number : "))
##
##def add(num):
##    if num==1:
##        return 1
##    else:
##        return num+add(num-1)
##print(add(num))


##start=int(input("Enter a Number to start addition : "))
##num=int(input("Enter a Number to end addition : "))
##
##def add(num, start):
##    if num==start:
##        return start
##    else:
##        return num+add(num-1,start)
##print(add(num,start))


##def f1(a,b):
##    a=a+10
##    b=b+10
##    c=a+b
##    return a,b,c
##
##data=f1(23,24)
##print(data)
##x,y,z=f1(10,20)
##
###this is tuple of size 1
##a=12
##print("%d is the number" %(34,))
##
##def addition(a=2,b=5,c=12,*t):
##    s=a+b+c
##    print(t)
##    for n in t:
##        s=s+n
##    return s
##print(addition(45))
##print(addition(10,23,4,5,2,3,1,2,6,7,8,9))

def delete(list1,val):
    
    c=list(list1).count(val)
    list1= list(filter(lambda x: x!=val, list1))
    
    return list1,val,c

list1=[1,12,20,25,20,5,2,21,21,20,1,12,25,22,20]

value= int(input("enter value to delete"))

print(delete(list1, value))





















    
