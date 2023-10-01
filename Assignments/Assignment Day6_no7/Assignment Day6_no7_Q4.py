set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print("intersection - ",set1.intersection(set2))
print("difference - ",set1.difference(set2)) 
print("union - ",set1.union(set2))  
print("differance - ",set1.difference(set2))
print("symmetric - ",set1.symmetric_difference(set2))
set1.symmetric_difference_update(set2)
print("symmetric_difference_update - ",set1)
set1.difference_update(set2) 
print("difference_update",set1) 