b = 50 #m
Q = 75 #m^3/s
g = 9.81 #m^2/s
n = 0.025
S0 = 0.001

#A = by + 1.5y^2
def A(y):
    A = (b*y) + (1.5 * (y**2))
    return A

#R = (by + 1.5y^2) / (b + 3.6y)
def R(y):
    R = A(y) / (b + (3.6*y))
    return R

#E = y + Q^2/2gA^2
def E(y):
    E = y + ( (Q**2) / (2 * g * A(y)) )
    return E

#S(f) = Q^2 * n^2 / R^4/3 * A^2
def Sf(y):
    soorat = Q**2 * n**2
    makhraj = (R(y)**(4/3)) * (A(y)**2)
    return soorat / makhraj

y1 = y2 = 12
delta_y = -0.5
x = 0 
#DX = DE / S0 - Sf

ertefa = []
tool = []

while y2 > 1:
    
    ertefa.append(y1)
    y2 = y1 + delta_y
    
    e1, e2 = E(y1), E(y2)
    delta_E = e2 - e1
    print("delta E = %f"%delta_E)
    Sf1, Sf2 = Sf(y1), Sf(y2)
    S_bar = 0.5 * (Sf1 + Sf2)
    
    makhraj = S0 - S_bar
    print("S0 - Sbar = %f"%makhraj)
    delta_x = delta_E / makhraj
    print("delta x = %f"%delta_x)
    tool.append(x)
    x += delta_x
    y1 += delta_y
    print()
'''
for i in range(len(tool)):
    print("ertefa = %f dar tool = %f"%(ertefa[i], tool[i]))
'''
#tool.sort()
import matplotlib.pyplot as plt
plt.plot(tool, ertefa, ".")
plt.grid(axis = "y")
plt.show()
input()