# Newton interpolation (output: Divided Difference Table &  y value given xp)
import numpy as np
def NewtonInterpolation(x,y,xp):
    #Create Divided Difference Table
    n=len(x)
    m=np.zeros((n,n+1))
    m[:,0]=x
    m[:,1]=y
    for i in range(1,n):
        for j in range(2,i+2):
            m[i,j]=(m[i,j-1]-m[i-1,j-1])/(m[i,0]-m[i-j+1,0])
    
    #Find value y given xp       
    S=m[0,1]
    for i in range(1,len(x)):
        L=1
        for j in range(1,i+1):
            L *= xp-m[j-1,0]
        S += L*m[i,i+1]
    return [m,S]


