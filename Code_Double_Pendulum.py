## Double Pendulum
import numpy as np
import sympy as smp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter

#Specified Arguments
t, g, m1, m2, L1, L2 = smp.symbols('t g m1 m2 L1 L2')

#Theta as Function of time
the1, the2 = smp.symbols(r'\theta_1, \theta_2', cls=smp.Function)
the1 = the1(t)
the2 = the2(t)

#Derivatives
the1_d = smp.diff(the1, t)
the2_d = smp.diff(the2, t)
the1_dd = smp.diff(the1_d, t)
the2_dd = smp.diff(the2_d, t)

#
x1 = L1*smp.sin(the1)
y1 = -L1*smp.cos(the1)
x2 = L1*smp.sin(the1)+L2*smp.sin(the2)
y2 = -L1*smp.cos(the1)-L2*smp.cos(the2)

#Kinetic Energy
T = (1/2 * m1 * (smp.diff(x1, t)**2 + smp.diff(y1, t)**2))+(1/2 * m2 * (smp.diff(x2, t)**2 + smp.diff(y2, t)**2))

#Potential Energy 
V = m1*g*y1 + m2*g*y2

#Lagrangian
L = T-V

#Solving For Derivative of Theta 1 and Theta 2 
Ltheta1 = smp.diff(L, the1) - smp.diff(smp.diff(L, the1_d), t).simplify()
Ltheta2 = smp.diff(L, the2) - smp.diff(smp.diff(L, the2_d), t).simplify()
sols = smp.solve([Ltheta1, Ltheta2], (the1_dd, the2_dd),simplify=False, rational=False)
dz1dt_f = smp.lambdify((t,g,m1,m2,L1,L2,the1,the2,the1_d,the2_d), sols[the1_dd])
dz2dt_f = smp.lambdify((t,g,m1,m2,L1,L2,the1,the2,the1_d,the2_d), sols[the2_dd])
dthe1dt_f = smp.lambdify(the1_d, the1_d)
dthe2dt_f = smp.lambdify(the2_d, the2_d)

#function 
def dSdt(S, t, g, m1, m2, L1, L2):
    the1, z1, the2, z2 = S
    return [
        dthe1dt_f(z1),
        dz1dt_f(t, g, m1, m2, L1, L2, the1, the2, z1, z2),
        dthe2dt_f(z2),
        dz2dt_f(t, g, m1, m2, L1, L2, the1, the2, z1, z2),
    ]

t = np.linspace(0, 20, 1000)
g = 9.81
m1=1
m2=1
L1 = 1
L2 = 1
ans = odeint(dSdt, y0=[np.pi/2, 0,(5/2)*(np.pi/2), 0], t=t, args=(g,m1,m2,L1,L2))

#List of x1, y1, x2, y2 respective to the Time(t)
def get(t, the1, the2, L1, L2):
    return (L1*np.sin(the1),
            -L1*np.cos(the1),
            L1*np.sin(the1) + L2*np.sin(the2),
            -L1*np.cos(the1) - L2*np.cos(the2))

x1, y1, x2, y2 = get(t, ans.T[0], ans.T[2], L1, L2)

#Animation
def animate(i):
    ln1.set_data([0,x1[i],x2[i]],[0,y1[i],y2[i]])

fig, ax=plt.subplots(1,1,figsize=(8,8))
ax.grid()
ln1, =plt.plot([],[],'ro-',lw=3,markersize=8)
ax.set_ylim(-4,4)
ax.set_xlim(-4,4)
ani=animation.FuncAnimation(fig,animate,frames=1000,interval=50)
ani.save('pen.gif',writer='pillow',fps=50)
