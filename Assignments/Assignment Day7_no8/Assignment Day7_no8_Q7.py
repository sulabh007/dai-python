sampleDict = {"Physics": 82,"Math": 65,"history": 75}

mark=0

for i,j in sampleDict.items():
    if j>mark:
        mark=j
        
print(mark)