s_mostatil = 80 #m^2
s_mosalas = 64 #m^2
masahat = [80 for i in range(7)]
masahat.append(64)
masahat.append(64)

v_mosalas = 3 #m/s
v_mostatil1 = 3.1
v_mostatil2 = 3.2
v_mostatil3 = 3.3
v_mostatil4 = 3.3
v_mostatil5 = 3.2
v_mostatil6 = 3.1
v_mostatil7 = 3.0

sorat = [3.0, 3.1, 3.2, 3.3, 3.3, 3.2, 3.1, 3.0, 3.0]
#----------------------------------------
#mohasebe alpha:
VA = 0
for i in range(len(sorat)):
    a = sorat[i] * masahat[i]
    VA += a
A_total = sum(masahat)
V3A = 0
for i in range(len(sorat)):
    a = (sorat[i]**3)* masahat[i]
    V3A += a
alpha = (V3A * (A_total**2)) / ((VA)**3)
#-----------------------------------
#mohasebe beta:
V2A = 0
for i in range(len(sorat)):
    a = (sorat[i]**2)* masahat[i]
    V2A += a
beta = (V2A * A_total) / (VA**2)

print("alpha = %f and beta = %f"%(alpha, beta))
input()