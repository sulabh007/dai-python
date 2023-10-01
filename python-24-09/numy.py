
import numpy as np


#identity matrix
a=np.identity(3)
print(a)

b=np.eye(3,4)
print(b)

b=np.eye(3,4,k=1)
print(b)

#filter the array
a=np.array([[12,13,14,15],[3,24,13,6],[10,18,4,12],[12,23,35,45]])
print(a[a%6==0])
print(a[a>5])

#to search the value
print(list(np.where(a%2==0)))

print(list(np.where(a%2==0)[0].data))
print(list(np.where(a%2==0)[1].data))


#to find sum of all values
print(a)
print(np.sum(a,axis=1)) #row wise sum
print(np.sum(a,axis=0))#column wise sum
print(np.sum(a)) #sum of all values

#to find mean
print(np.mean(a))

print(np.median(a))

#hstack and vstack
x=np.array([10,20,30])
y=np.array([11,12,13])
z=np.array([21,22,23])

#to arrange data horozontlly
print(np.hstack((x,y,z)))

d=np.vstack((x,y,z))
print(d)

#reverse columns and rows both
print(d)
print(np.flip(d)) #reverse rows and columns both
print(np.flip(d,axis=0)) #reverse only rows
print(np.flip(d,axis=1)) #reverse only columns

#endpoint=False will exclude 30
x=np.linspace(10,30,7, endpoint=False)
print(x)
