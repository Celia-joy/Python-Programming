import numpy as np
print("Enter the temperature in degree celcius: ")
celsius= float(input())
kelvin = celsius + 273.15 
fahrenheit = (celsius*9/5)+32
print("The temperature in kelvin is: ", kelvin)
print("The temperature in fahrenheit is: ", fahrenheit)

print("Enter the polar coordinates: ")
print("r:")
r = float(input())
print("thetha:")
thetha = float(input())
x= r*np.cos(thetha)
y= r*np.sin(thetha)
print("The cartesian coordinates are: ", x,"and", y)


print("Enter the cylindrical coordinates:")
r= float(input("r:"))
thetha = float(input("thetha:"))
z= float(input("z:"))

x= r*np.cos(thetha)
y= r*np.sin(thetha)
z=z
print("The cartesian coordinates are:", x,y,z)

import matplotlib.pyplot as plt
Qo = 5*10**-6
omega = 100*np.pi
T= 2*np.pi/omega
t= np.linspace(0, 2*T, 100)
Q = Qo*np.sin(omega*t)

plt.plot(t,Q)
plt.grid()
plt.show()
