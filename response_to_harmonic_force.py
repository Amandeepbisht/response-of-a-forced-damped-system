


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib import interactive

def model(x,t):
    y = x[0]
    dy = x[1]
    xdot = [[],[]]
    xdot[0] = x[1]
    xdot[1] = -((50/51)*(dy)) - ((112.5/51)*y) + ((50/51)*(np.sin(21*t)))
    return (xdot)


t = np.linspace(0,15,1000)

sol = odeint(model,[0.1,0.04],t)
print (sol[:,1])

plt.plot(t,sol[:,1])
plt.xlabel("time(seconds)")
plt.ylabel("distance(meters)")
plt.grid()
interactive(True)
plt.show()



'''def function(y):
    z = (1-y**2)**2 + (2*0.33*y)**2
    return (1/np.sqrt(z))

w = np.linspace(0,140,500)


plt.plot(w,function(w))
plt.xlabel("w/wn")
plt.ylabel("A/Xs")
plt.grid()
interactive(False)
plt.show()'''















