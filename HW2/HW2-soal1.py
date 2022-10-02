#------------------
beta = 1
qstar = 0.2
g = 9.81
b = 15
T = b
n = 0.013
l = 35
s0= 0.021
#-------------------
Q = 4.85 #assumed 
q = Q / b
yc = ((q**2) / g)**(1/3)
P = (2 * yc) + 15
R = (yc * b) / ((2 * yc) + 15)
#-------------------
parantez = ( s0 - (((n**2) * g * P) / (beta * T * (R**(1/3)) )) )**3 
makhraj = g * (T**2) * parantez
soorat = 8 * beta * (qstar**2)
#-------------------------------
x = soorat / makhraj
print("x is %f meter"%x)
print("Q is %f m^3/s and yc equal to %f meter"%(qstar*x,yc))
#------------------------
import pandas as pd
import numpy as np
a = pd.DataFrame()