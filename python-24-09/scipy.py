from scipy.special import cbrt,comb,perm
x=cbrt([27,64])
print(type(x))
print(x)

print(perm(6,2))
print(comb(6,2))

import numpy as np
from scipy import linalg
m=np.array([[10,20],[30,40]])
print(linalg.det(m))

eig_val,eig_vect=linalg.eig(m)
print(eig_val,eig_vect)

from scipy import stats
m=np.array([[22,23,14,22,56],[22,46,23,14,34]])
modeval=stats.mode(m,axis=1)
print(modeval)



from scipy import integrate
#take f(x) fuction as f
f = lambda x : x**2
#singel integration wit a=0 & b=0
integration = integrate.quad(f,0,1)
print(integration)