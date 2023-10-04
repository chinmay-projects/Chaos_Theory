

#Lorentz Attractor

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Lorenz system of equations
def lorenz(t, xyz, sigma, rho, beta):
    x, y, z = xyz
    Dx = sigma * (y - x)
    Dy = x * (rho - z) - y
    Dz = x * y - beta * z
    return [Dx,Dy,Dz]

# Parameters
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Initial conditions
xyz1 = [1.0, 0.0, 0.0]
xyz2 = [1.000001, 0.0, 0.0]
xyz3 = [0.9999, 0.0, 0.0]

# Time Period
t_span = (0, 50)
t_eval = np.linspace(*t_span, 10000)

# Data set of the Lorenz equations
sol1 = solve_ivp(lorenz, t_span, xyz1, args=(sigma, rho, beta), t_eval=t_eval)
sol2 = solve_ivp(lorenz, t_span, xyz2, args=(sigma, rho, beta), t_eval=t_eval)
sol3 = solve_ivp(lorenz, t_span, xyz3, args=(sigma, rho, beta), t_eval=t_eval)

# Plotting
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot( projection='3d')
ax.plot(sol1.y[0], sol1.y[1], sol1.y[2], lw=0.5 , color='#000000')
ax.plot(sol2.y[0], sol2.y[1], sol2.y[2], lw=0.5 , c = '#FFA500')
ax.plot(sol3.y[0], sol3.y[1], sol3.y[2], lw=0.5 , c = 'r')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Lorenz Attractor')
plt.show()
    
    

