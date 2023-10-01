################################Q1#############################################

# import re

# mob=input("Enter mobile number : ")

# num=re.match("\d{10}", mob)

# if num!=None:
#     print("Mobile number is valid")
# else:
#     print("Mobile number is not valid")
    
################################Q2a#############################################

# import re
# lst=[]
# with open("product.txt", "r") as fh:
#     with open("myproduct.txt", "w") as fh1:
#         for line in fh:
#             match=re.match("^12.*0$", line)
#             if match!=None:
#                 fh1.write(line)
 
################################Q2b#############################################
                
# dict1={}
# with open("product.txt", "r") as fh:
#     with open("myproduct.txt", "w") as fh1:
#         for line in fh:
#             lst=list(line.split(":"))
#             #lst[4]=lst[4].strip("\n")
#             dict1.setdefault(lst[3],0)
#             dict1[lst[3]]=int(dict1[lst[3]])+int(lst[4])
            
# print(dict1)

################################Q2c#############################################

import re

cat=str(input("Enter Category : "))
with open("product.txt", "r") as fh:
    for line in fh:
        match=re.search(cat, line, re.I)
        if match:
            print(line)








