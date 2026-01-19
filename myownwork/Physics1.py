from math import (radians, sin, asin, cos, sqrt)
def distance(lat1, lat2, lon1, lon2):
    R = 6371
    lat1, lat2, lon1, lon2 = map(radians, [lat1, lat2, lon1, lon2])
    a = sin((lat2-lat1)/2)*sin((lat2-lat1)/2)+ cos(lat1)*cos(lat2)*sin((lon2-lon1)/2)*sin((lon2-lon1)/2)
    return 2*R*asin(sqrt(a))

print((distance(-1.994, -1.292, 30.062, 36.822)), "km")

import numpy as np 
rho = 5
theta = 60
z = 2

x= rho*cos(theta)
y= rho*sin(theta)
z=z
print(f"x={x}, y={y}, z={z}")

import numpy as np
x1 = 15600000
y1 = 7540000 
z1 = 20140000
r_i1 = 21400000

x2 = 18760000
y2 = 2750000
z2 = 18600000
r_i2 = 21350000

x3 = 17600000
y3 = 14600000
z3 = 13400000
r_i3 = 21100000

x4 = 19170000
y4 = 6100000 
z4 = 18390000
r_i4 = 21490000

G1= (x1, y1, z1, r_i1)
G2= (x2, y2, z2, r_i2)
G3= (x3, y3, z3, r_i3)
G4= (x4, y4, z4, r_i4)

c = 3*100000000
x_i1 = float (input ("x_i1:"))
y_i1 = float (input ("y_i1:"))
z_i1 = float (input ("z_i1:"))

x_i2 = float (input ("x_i2:"))
y_i2 = float (input ("y_i2:"))
z_i2 = float (input ("z_i2:"))

x_i3 = float (input ("x_i3:"))
y_i3 = float (input ("y_i3:"))
z_i3 = float (input ("z_i3:"))

x_i4 = float (input ("x_i4:"))
y_i4 = float (input ("y_i4:"))
z_i4 = float (input ("z_i4:"))

dt = float (input ("dt:"))
print(((x1-x_i1)*(x1-x_i1))+((y1-y_i1)*(y1-y_i1))+((z1-z_i1)*(z1-z_i1)))==(r_i1-(c*dt))*(r_i1-(c*dt))
print(((x2-x_i2)*(x2-x_i2))+((y2-y_i2)*(y2-y_i2))+((z2-z_i2)*(z2-z_i2)))==(r_i2-(c*dt))*(r_i2-(c*dt))
print(((x3-x_i3)*(x3-x_i3))+((y3-y_i3)*(y3-y_i3))+((z3-z_i3)*(z3-z_i3)))==(r_i3-(c*dt))*(r_i3-(c*dt))
print(((x4-x_i4)*(x4-x_i4))+((y4-y_i4)*(y4-y_i4))+((z4-z_i4)*(z4-z_i4)))==(r_i4-(c*dt))*(r_i4-(c*dt))


x1 = float (input("A_x:"))
y1=  float (input("A_y:"))
z1 = float (input("A_z:"))
x2 = float (input("B_x:"))
y2 = float (input("B_y:"))
z2 = float (input("B_z:"))
dot_product = x1*x2+ y1*y2+ z1*z2
print("dot_product=" , dot_product )

Ax= float (input("Ax:"))
Ay= float (input("Ay:"))
Az= float (input("Az:"))
Bx= float (input("Bx:"))
By= float (input("By:"))
Bz= float (input("Bz:"))
cross_product1 = (Ay*Bz-(Az*By))
cross_product2 = (Ax*Bz-(Az*Bx))
cross_product3 = (Ax*By-(Ay*Bx))
print(f"The cross product = ", cross_product1 ,"i+", cross_product2 , "j+", cross_product3 ,"k")

import math
r= float (input("r="))
thetha_deg= float(input("thetha_deg="))
thetha_rad= math.radians(thetha_deg)
x= r*cos(thetha_rad)
y= r*sin(thetha_rad)
print(f"x={x},y={y}")

import math
rho= float(input("rho=")) 
thetha_deg= float(input("thetha_deg="))
z= float (input("z="))
thetha_rad = math.radians(thetha_deg)
x= rho*cos(thetha_rad)
y= rho*cos(thetha_rad)
z=z
print(f"x={x}, y={y}, z={z}")
