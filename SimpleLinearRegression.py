#Simple Linear equation. x, y are array
import numpy as np
def SimpleLinearRegression(x,y):
    x,y=np.array(x),np.array(y)
    a=(np.mean(y)*(sum(x**2))-np.mean(x)*sum(x*y))/(sum(x**2)-len(x)*(np.mean(x))**2)
    b=(sum(x*y)-np.mean(x)*sum(y))/(sum(x**2)-len(x)*(np.mean(x))**2)
    return a,b
