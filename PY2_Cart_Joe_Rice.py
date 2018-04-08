#Joseph Rice
#1/25/2018
# Python #2 Modeling motion 
from __future__ import division 
from visual import *
#2) initial statements
track = box(pos=vector(0,-.05,0),size=(2.0,0.05,.10),color=color.cyan)
cart = box(pos=vector(1-0.04,0,0),size=(0.1,0.04,0.06),color=color.red)

""" Int conditions"""
# mass of cart 
cart.m = 0.80
#momentume of the cart 
cart.p = cart.m* vector(-1*0.5, 0,0)
print('cart momentum =', cart.p)
print('test =', 0.5*0.80)
# incriments the time by 0.01
deltat = 0.01
t=0
#3) update statements
F_air = vector(0.052,0,0)
while t < 15.3:
    rate(100)
    print('the time is now',t )
    
    F_net = F_air
    #Momentum Principle
    cart.p += F_net*deltat
    
    ## Update position equation 
    cart.pos = cart.pos +  (cart.p/cart.m)  * deltat

    ### Time update 
    t += deltat

    
print('after the loop')



