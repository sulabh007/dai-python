import functools
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

sum1=functools.reduce(lambda a,b:a+b,set1)
avg=sum1/len(set1)
print(avg)
set1.update((filter(lambda x:x>avg,set2)))

print(set1)