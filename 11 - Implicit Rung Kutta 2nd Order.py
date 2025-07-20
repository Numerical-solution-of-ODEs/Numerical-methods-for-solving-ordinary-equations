import numpy as np
from numpy import sin
from numpy import cos
from numpy import tan
from numpy import sinh
from numpy import cosh
from numpy import tanh

from matplotlib import pyplot as plt

def calculate(value1, value2, function):
    x = value1
    y = value2
    return eval(function)

def imp_rung_2 (x0 , y0 , h, n , f):
    z=np.zeros(2)
    k=np.zeros(2)
    y=np.zeros(n+1)
    y[0]=y0

    for i in range (0 , n):
        z[0]= y[i]
        z[1]= y[i]+(1/2)*h*calculate(x0+i*h , y[i] , f)

        k[0] = y[i] + (1/4)* h *(calculate( x0+i*h , z[0] , f) - calculate(x0+ (i+ 2/3 )*h , z[1] , f))
        k[1] = y[i] + (1/12)*h *(3* calculate (x0+i*h , z[0] , f )+ 5* calculate(x0+(i+2/3)*h , z[1] , f))

        y[i+1]= y[i] + (1/4)*h *(calculate(x0+i*h , k[0], f)+ 3* calculate(x0+(i+2/3)*h , k[1] , f))
        
        print('y %i = %f' % (i+1, y[i+1]))

    x=np.zeros(n+1)
    for i in range(0,n+1):
        x[i]=x0 + h * i

    plt.plot(x, y, 'r')
    plt.show()

f = str(input("If y'=f(x,y) , Please Enter f(x,y) : \n", ))
x = float(input("Please Enter x0 :\n"))
y = float(input("Please Enter y0 :\n"))
h = float(input("Please Enter Step Lenth (h) :\n"))
n = int(input("Please Enter Number Of Steps (n) : \n"))
imp_rung_2(x, y, h, n, f)
input("Click Enter To Close.")

