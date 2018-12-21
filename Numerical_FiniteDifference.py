f=lambda x: 0.1*x**5-0.2*x**3+0.1*x-0.2
h=0.0001
x=0.1


#Forward finite difference approximation
dff1=(f(x+h)-f(x))/h
dff2=(f(x+2*h)-2*f(x+h)+f(x))/h**2

print('1st derivative at {:5f} is {:5f}, 2nd derivative is {:5f} '.format(x,dff1,dff2))


#Central finite difference approximation
dfc1=(f(x+h)-f(x-h))/(2*h)
dfc2=(f(x+h)-2*f(x)+f(x-h))/(h**2)
print('1st derivative at {:5f} is {:5f}, 2nd derivative is {:5f} '.format(x,dfc1,dfc2))


#Backward finite difference approximation
dfb1=(f(x)-f(x-h))/h
dfb2=(f(x)-2*f(x-h)+f(x-2*h))/(h**2)
print('1st derivative at {:5f} is {:5f}, 2nd derivative is {:5f} '.format(x,dfb1,dfb2))

#Use derivative function
dfc1=derivative(f,x,h,1) #1st derivative
dfc2=derivative(f,x,h,2) #2nd derivative