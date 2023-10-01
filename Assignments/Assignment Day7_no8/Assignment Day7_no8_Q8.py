sampleDict = {"emp1": {"name": "Jhon", "salary": 7500},"emp2": {"name": "Emma", "salary": 8000},"emp3": {"name": "Brad", "salary": 6500}}

name=str(input("Enter name of employee : "))
# for i in sampleDict.keys():
#     print(f"i {i}")
#     if name==sampleDict[i]["name"]:#.get("name"):
#         print("name found")
#     else:
#         print("Name no found")
    # for j in sampleDict[i].keys():
    #     print(j)
    # for k,l in j.items():
    #     #print(f"k {k} - l {l}")
    #     if l==name:
    #         print("Name found")
    #         break
    #     else:
    #         print("Name not found")
            
    
sal=int(input("Enter new salary : "))
# # name="Jhon"
# # sal=45644
notfoud=0
# for i,j in sampleDict.items():
#         #print(f"i {i} - j {j}")
#         for k,l in j.items():
#             #print(f"k {k} - l {l}")
#             if l==name:
#                 oldsal=sampleDict[i].get("salary")
#                 if oldsal>sal:
#                     print("Wrong salary entered")
#                     break
#                 sampleDict[i]["salary"]=sal
#                 print("Salary Updated")
#             elif l!=name:
#                 notfoud=1
# if notfoud==1:
#     print("Name not found")              
# print(sampleDict)    

for i,j in sampleDict.items():
    if j["name"]==name:
        oldsal=sampleDict[i].get("salary")
        if oldsal>sal:
            print("Wrong salary entered")
            break
        sampleDict[i]["salary"]=sal
        print("Salary Updated")
        break
    else:
        notfoud=1
if notfoud==1:
    print("Name not found")              
print(sampleDict)       