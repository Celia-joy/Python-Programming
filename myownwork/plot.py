#this code represents the charge
#this given by Q= Qo sin * omega*t
import numpy as np
import matplotlib.pyplot as plt
Qo = 5*(10**(-6))
omega = 100 * np.pi
T = 2*np.pi/omega
t = np.linspace(0, 2*T, 100)
Q = Qo*np.sin(omega*t)
plt.plot(t, Q)
plt.grid()
plt.show()