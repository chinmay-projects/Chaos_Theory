# Rössler Attractor

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Functon for Rossler Equations 
def rössler(t,xyz,a,b,c):
    x, y, z = xyz
    Dx=-y-z
    Dy=x+(a*y)
    Dz=b+(z*(x-c))
    return [Dx,Dy,Dz]

#Parameters
a,b,c=0.1,0.1,14.0

#Initial Conditions
xyz1=[1.0,0.0,0.0]

# Time Period
t_span = (0,1000)
t_eval = np.linspace(*t_span, 1000000)

#Chaos Data
sol1 = solve_ivp(rössler, t_span, xyz1, args=(a,b,c), t_eval=t_eval)

#Plotting
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot( projection='3d')
ax.plot(sol1.y[0], sol1.y[1], sol1.y[2], lw=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Rössler Attractor')
plt.show()
