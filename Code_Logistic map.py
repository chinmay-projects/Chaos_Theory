#Logistic Map
import matplotlib.pyplot as plt
import numpy as np

#Function 
def function (a,x):
    f=a*x*(1-x)
    return f

#Chaos Function
def chaos(a,xi,n):
    x=xi
    x_value=[]
    y=[]
    for i in range(n):
        x_value.append(x)
        x=function(a,x)
    return x_value

#Initial conditions
xi=0.5
a=3.9
n=25
x=np.linspace(0,n,n)

#Chaos Data
x1_value=chaos(a,xi,n)
x2_value=chaos(a,xi+0.01,n)
x3_value=chaos(a,xi+0.001,n)

#Plotting
fig = plt.figure(figsize=(12, 9))
plt.plot(x,x1_value)
plt.plot(x,x2_value)
plt.plot(x,x3_value)
plt.show()



