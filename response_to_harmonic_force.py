import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model(x,t): # Function that defines the differential equation of the problem
    y = x[0]
    dy = x[1]
    xdot = [[],[]]
    xdot[0] = x[1]
    xdot[1] = -((50/51)*(dy)) - ((112.5/51)*y) + ((50/51)*(np.sin(21*t)))
    return (xdot)


t = np.linspace(0,15,1000) 

sol = odeint(model,[0.1,0.04],t) #solver function that solves the differential equation defined above
print (sol[:,1])

plt.plot(t,sol[:,1])
plt.xlabel("time(seconds)")
plt.ylabel("distance(meters)")
plt.grid()
plt.show()


















