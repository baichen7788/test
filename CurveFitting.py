#Curve fitting( m is number of data points, n is degree of curve fitting)
import numpy as np
def CurveFit(x,y,n):
    m=len(x)
    x,y=np.array(x),np.array(y)
    A=np.zeros((n+1,n+1))
    B=np.zeros(n+1)
    for row in range(n+1):
        for col in range(n+1):
            if row==col==0:
                A[row,col]=m
                continue
            A[row,col]=np.sum(x**(row+col))
        B[row]=np.sum(x**row*y)
    return np.linalg.solve(A,B)   # output is coefficient of the curve fitting equation
        
x=np.arange(6)
y=[2,8,14,28,39,62]
CurveFit(x,y,2)