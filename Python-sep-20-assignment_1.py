import re 
add=0 
fh=open("data20.txt","r")
sal=[]
dep=[]
dict1={}
for line in fh:
    lst=line.strip("\n").split(r":")
    sal.append((lst[4],lst[3]))
    dep.append(lst[4])

dict1=dict.fromkeys(dep,0)

for i,j in sal: 
    dict1[i]=dict1[i]+int(j)
print(dict1)

fh.close()

