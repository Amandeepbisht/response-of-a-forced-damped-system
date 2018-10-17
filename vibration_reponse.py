import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def function(y): # function that defines A/Xs in terms of w/wn (wn = natural frequency, w = varying input frequency)
    z = (1-y**2)**2 + (2*0.33*y)**2
    return (1/np.sqrt(z))

w = np.linspace(0,70,500) # here '70' is the 104/wn (wn = natural frequency of the system) and 500 is the number of divisions from 0 to 70


plt.plot(w,function(w))
plt.xlabel("w/wn")
plt.ylabel("A/Xs")
plt.grid()

plt.show()
