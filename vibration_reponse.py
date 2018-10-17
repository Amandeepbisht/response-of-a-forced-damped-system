import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def function(y):
    z = (1-y**2)**2 + (2*0.33*y)**2
    return (1/np.sqrt(z))

w = np.linspace(0,140,500)


plt.plot(w,function(w))
plt.xlabel("w/wn")
plt.ylabel("A/Xs")
plt.grid()

plt.show()
