set1=set()
n=int(input("Enter value of n :"))
str1=str(input("Enter string :"))

while str1!="":
    set1.add(str1)
    str1=str(input("Enter string :"))
    
set2=set(filter(lambda x:len(x)>n, set1))
print(set2)


