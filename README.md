# Chaos_Theory
Chaos theory is a branch of mathematics and physics that deals with complex systems whose behavior is highly sensitive to initial conditions. It essential describes how relativily simple systems can exhibit extremely complex and unpredectible motion. 

## Logistic Map
Logistic map shows that the behavior of dynamic systems are highly sensitive to initial conditions. It illustrates how a simple nonlinear equation can lead to complex, unpredictable outcomes. 

The logistic map is defined as:
$$x_m=ax_n(1-x_n) , m=n+1$$

![Figure_2](https://github.com/chinmay-projects/Chaos_Theory/assets/125910307/aaf2568b-cc36-464f-9b01-bf33e730a6b4)


The plotted data vividly illustrates the sensitivity of the logistic map to initial conditions. Even a minute difference in the initial value leads to drastically different outcomes over iterations.

## Rössler Attractor
The Rössler attractor is a  system of three non-linear ordinary differential equations and another fascinating example of chaotic behavior in dynamical systems.
Rössler Equations are as follow :
$$\frac{dx}{dt} = -y-z $$

$$\frac{dy}{dt} = x + ay$$

$$\frac{dz}{dt} = b+z \cdot(x-c)$$
 The parameters a = 0.1, b = 0.1 and c = 14.0 were chosen to simulate the attractor. The resulting trajectory of the system was plotted in 3D space to visualize its behavior.


## Lorentz Attractor (Butterfly Effect)
The Lorenz attractor is a set of chaotic solutions to a system of three non-linear differential equations. It was first studied by Edward Lorenz in 1963 as a simplified model of atmospheric convection, but it has since become a classic example of chaotic systems in mathematics and physics.

The Lorenz system of equations is given by:

$$\frac{dx}{dt} = \sigma \cdot (y-x)$$

$$\frac{dy}{dt} = x \cdot ( \rho -z)-y$$

$$\frac{dz}{dt} = x \cdot y - \beta \cdot z$$

where x, y and z are the variables of the system, and $\sigma$, $\rho$, and $\beta$ are parameters. The system exhibits chaotic behavior for certain values of these parameters. In the code you provided, the parameters are set to $\sigma$ = 10.0 , $\rho$ = 28.0 , $\beta$ = 8.0 / 3.0 which are the commonly used values to visualize the Lorenz attractor.

![Figure_3](https://github.com/chinmay-projects/Chaos_Theory/assets/125910307/54a2ffd2-87fc-40c0-a8d7-e4477e2fb6e4)

## Double Pendulum
A double pendulum is a physical system where two pendulums are attached end-to-end. The motion of the second pendulum is influenced by the motion of the first pendulum, creating a complex and chaotic behavior. The equations governing the motion of a double pendulum are highly nonlinear and can exhibit sensitive dependence on initial conditions, leading to chaotic motion.




The equations of motion for the double pendulum are derived from the Lagrangian of the system, which represents the difference between its kinetic and potential energies. The Lagrange's equations yield a set of second-order ordinary differential equations that describe how the angles and angular velocities of the pendulums change over time.

$$\\frac{\\partial L}{\\partial \\theta_1} - \\frac{d}{dt}\\frac{\\partial L}{\\partial \\dot{\\theta_1}} = 0$$

$$\\frac{\\partial L}{\\partial \\theta_2} - \\frac{d}{dt}\\frac{\\partial L}{\\partial \\dot{\\theta_2}} = 0$$

