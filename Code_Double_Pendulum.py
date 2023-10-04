import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Function defining the double pendulum system of ODEs
def double_pendulum(t, y, l1, l2, m1, m2, g):
    theta1, omega1, theta2, omega2 = y
    dydt = [omega1,
            (-g * (2 * m1 + m2) * np.sin(theta1) - m2 * g * np.sin(theta1 - 2 * theta2) - 2 * np.sin(theta1 - theta2) * m2 * (omega2**2 * l2 + omega1**2 * l1 * np.cos(theta1 - theta2))) /
            (l1 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2))),
            omega2,
            (2 * np.sin(theta1 - theta2) * (omega1**2 * l1 * (m1 + m2) + g * (m1 + m2) * np.cos(theta1) + omega2**2 * l2 * m2 * np.cos(theta1 - theta2))) /
            (l2 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2)))]
    return dydt

# Parameters
l1 = 1.0  # Length of pendulum 1
l2 = 1.0  # Length of pendulum 2
m1 = 1.0  # Mass of pendulum 1
m2 = 1.0  # Mass of pendulum 2
g = 9.81  # Acceleration due to gravity

# Initial conditions [theta1, omega1, theta2, omega2]
initial_conditions = [np.pi / 2, 0, np.pi, 0]  # Pendulums initially at rest

# Time span
t_span = [0, 10]
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Solve the ODEs for the double pendulum system
solution = solve_ivp(lambda t, y: double_pendulum(t, y, l1, l2, m1, m2, g),
                     t_span, initial_conditions, t_eval=t_eval, method='DOP853')

# Extracting the angles for plotting
theta1 = solution.y[0]
theta2 = solution.y[2]

# Plotting the chaotic motion of the double pendulum
plt.figure(figsize=(8, 6))
plt.plot(theta2, theta1, linewidth=0.5)
plt.xlabel('Theta 1 (radians)')
plt.ylabel('Theta 2 (radians)')
plt.title('Chaotic Motion of Double Pendulum')
plt.show()