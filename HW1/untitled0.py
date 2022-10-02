Q = 1000
#q = Q / b
qs = []
from numpy import arange, roots
for i in arange(8.3, 10, 0.1):
    b = i
    q = Q/b
    qs.append(q)
#print(qs)
#---------------------------------
E = 10.55
Q = 1000
g = 32.2
Bs = []
for i in arange(8.3, 10, 0.1):
    Bs.append(i)
kol = []
for b in Bs:
    
    javab = roots([2*g*b, -(10.55 * 2 * g * b), 1000**2])
    kol.append(javab)
#print(kol)
for i in kol:
    print(i)