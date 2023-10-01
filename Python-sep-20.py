#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:44:19 2023

@author: dai
"""
import re
str1="Something is there Somewhere"

m=re.match(r"\bt.*?e\b",str1,re.I|re.M)
if m != None:
    print(m.group())
    print(m.span())
else:
    print("Not found")
    
m=re.search(r"\bt.*?e\b",str1,re.I|re.M)
if m != None:
    print(m.group())
    print(m.span())
else:
    print("Not found")
    
lstmatch=re.finditer("s.*?e",str1,re.I|re.M)
if lstmatch!=None:
    for m in lstmatch:
        print(m.group())
        print(m.span())
    else:
        print("Not found")
 
lst=re.findall("s.*?e",str1,re.I|re.M)
if lst!=None:
        print(lst)
else:
        print("Not found")
        
        
str1="Something is there Somewhere"       
s1=re.sub("s.*?e","any",str1,flags=re.I|re.M,count=2)
print(s1)      
        
myreg=re.compile("s.*?e",re.I|re.M)
       
str1="Something is there Somewhere"            
myreg.findall(str1)
if lst!=None:
        print(lst)
else:
        print("Not found")       
       
        
        
mob=input("Enter Mobile No. :")
m=re.match("[987]\d{9}",mob)
if m!=None:
    print("Mobile Number is valid")    
else:
    print("Not Found")
        
mob=input("Enter Mobile No. :")
m=re.match("\+{2,4}-{987}\d{9}",mob)
if m!=None:
    print("Mobile Number is valid")    
else:
    print("Not Found")        
        
        
s="This is home"
m=re.match("^\w+\s\w+\s\w+$",s)
if (m!=None):
    print("found")
else:
    print("Not found")
        
s="This is home"
m=re.match("^(\w+)\s(\w+)\s(\w+)$",s)
if m!=None:
    print(m.group(),m.span())
    print(m.group(1),m.span(1))
    print(m.group(2),m.span(2))
    print("found")
else:
    print("Not found")
               
ac="xxxx1234xxxx"
m=re.match("x{4}(\d{4})x{4}", ac)
if m!=None:
    print(m.group(1),m.span(1))
else:
    print("Not found")
###############################File Handling####################################    
lst=[]       
fh=open("mydata.txt")
for line in fh:
    line=line.rstrip("\n")      
    print(line)
    lst.append(line)
print(lst)
        
fh=open("mydata.txt","r")
fh1=open("mycopy.txt","w")
for line in fh:
    fh1.write(line)  
fh.close()
fh1.close()


import re  
fh=open("mydata.txt","r")
fh1=open("mycopy.txt","w")
for line in fh:
    if re.search("game", line):
        fh1.write(line)  
fh.close()
fh1.close()     


import re  
fh=open("mydata.txt","r")
fh1=open("mycopy.txt","w")
for line in fh:
    lst=line.split(":")
    if lst[2]=="game":
        fh1.write(line)
fh.close()
fh1.close()  
 
import re  
fh=open("mydata.txt","r")
fh1=open("mycopy.txt","w")
for line in fh:
    lst=line.split(":")
    if re.search("game", lst[3]):
        fh1.write(line)
fh.close()
fh1.close()  
       
        

import re  
with open("mydata.txt","r") as fh:
    with open("mycopy.txt","w") as fh1:
        for line in fh:
            lst=line.split(":")
            if lst[2]=="game":
                fh1.write(line)

import re 
add=0 
fh=open("mydata.txt","r")
for line in fh:
    lst=line.split(":")
    add=add+int(lst[4])
print(add)     
fh.close()
 
               
fh=open("mydata.txt","r")  
lst=fh.readline()
print(lst)     
fh.close()       
        
fh=open("mydata.txt","r")  
s=fh.read(7)
print(fh.tell())     
fh.close()  
































        