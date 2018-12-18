
#Lagrange Interpolation
x=[0,20,40,60,80,100]
y=[20,48.6,61.6,71.2,74.8,75.2]

n=len(x)
xp=50
yp=0
for i in range(n):
    L=1
    for j in range(n):
        if j != i:
            L *= (xp-x[j])/(x[i]-x[j])
    yp += y[i]*L
print(yp)