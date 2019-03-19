#InitVelFinder.py
#Shrey Mahey
#Finds initial velocity of a projectile given dx,dy, and theta
#Assumes projectile has been shot out from our ramp specifically
from math import cos,sin,tan,radians,sqrt,floor,log10
theta,d_clamp,h_clamp = map(int,input().split(" "))

d_ramp = 19.865
d_launch = 16.8275*cos(radians(theta))

h_ramp = 6.3975
h_launch = 16.8275*sin(radians(theta))

def r(x,sigdig=5):
    return round(x,sigdig-int(floor(log10(abs(x))))-1)

dx = r(d_clamp + d_ramp - d_launch)
dy = r(((h_clamp - h_ramp - h_launch)*-1))
vt = r(((dx)/(cos(radians(theta)))))
t = r((sqrt((vt*sin(radians(theta)) + dy)/490.5)))
v = r((vt/t))
print("velocity",r(v/100))
