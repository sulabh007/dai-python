str1 = str(input("Enter a string :"))
check = str(input("Enter a word to find :"))
cnt = 0
pos = str1.find(check)

while pos != -1:
    print(check, "-", pos)
    pos = str1.find(check,pos+1)
    cnt = cnt + 1
print(f"Count :{cnt}")