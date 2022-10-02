import numpy as np
import matplotlib.pyplot as plt
z = []
moadelat = [[] for i in range(13)]
for i in range(len(moadelat)):
    delta_z = 0.1 + (0.1 * i)
    z.append(delta_z)
    moadelat[i] = [1, -(11.55 - delta_z), 0, 155.28]
javab = []
for coef in moadelat:    
    a = np.roots(coef)
    javab.append(a)
accepted = []
for each in javab:
    accepted.append(each[0])
plt.plot(z, accepted)
plt.ylabel("delta_z")
plt.xlabel("y2")
plt.grid()
plt.show()