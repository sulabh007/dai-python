sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
temp=""
temp=sampleDict.get("city")
sampleDict.pop("city")
sampleDict.setdefault("location",temp)
print(temp)
print(sampleDict)