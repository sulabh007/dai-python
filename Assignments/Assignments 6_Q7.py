
lst=[]
num=input("Enter a number :")

while num!="q":
    lnum=int(num)%10
    for i in range(len(lst),lnum+1):
        lst.append([])
    lst[lnum].append(num)
    num=input("Enter a number :")
    
print(lst)

