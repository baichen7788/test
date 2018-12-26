#Trapezoidal rule.  By inceasing n, Integral will approach to true integral value
from math import sin,pi
f=lambda x : x*sin(x)

a,b =0,pi/2
n=1000000
h=(b-a)/n

s=0.5*(f(a)+f(b))
for i in range(1,n):
    s += f(a+i*h)
Integral=h*s
Integral



# Simpson's 1/3 rule , n must be even number
from math import sin,pi
f=lambda x : x*sin(x)

a,b =0,pi/2
n=1000000
h=(b-a)/n

s=(f(a)+f(b))
for i in range(1,n,2):
    s += 4*f(a+i*h)
for i in range(2,n,2):
    s += 2*f(a+i*h)
Integral=h/3*s
Integral



# Simpson's 3/8 rule , n must be multiple of 3  less accurate than 1/3 rule
from math import sin,pi
f=lambda x : x*sin(x)

a,b =0,pi/2
n=999
h=(b-a)/n

s=(f(a)+f(b))
for i in range(1,n,3):
    s += 3*(f(a+i*h)+f(a+(i+1)*h))
for i in range(3,n,3):
    s += 2*f(a+i*h)
Integral=3*h/8*s
Integral





#Double integral using Simpson's 1/3 rule

f=lambda x, y: x**2*y+x*y**2

ax=1
bx=2
ay=-1
by=1
nx=10
ny=10

hx=(bx-ax)/nx
hy=(by-ay)/ny

s=0
for i in range(0,ny+1):
    if i==0 or i==ny:
        p=1                     #p is factor
    elif i%2 ==1 :
        p=4
    else:
        p=2
    for j in range(0,nx+1):
        if j == 0 or j == nx:
            q=1                #q is factor
        elif j%2 ==1 :
            q=4
        else:
            q=2
        s += p*q*f(ax+j*hx,ay+i*hy)
Integral=s*hx*hy/9
Integral




###Integral using Scipy
from scipy.integrate import quad,dblquad,nquad
import numpy as np


#Single integral
f=lambda x: x*np.sin(x)
I,_=quad(f,0,np.pi/2)    # _ means that value is ignored
I


# Double integral
fn=lambda x,y: x**2*y+x*y**2
ax,bx=1,2
ay,by=-1,1

I,_=dblquad(fn,ax,bx,lambda y:ay,lambda y: by)
I


#N quad integral
nquad(f,[[0,np.pi/2]])
nquad(fn,[[ax,bx],[ay,by]])
