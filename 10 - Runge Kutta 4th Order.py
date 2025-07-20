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

def rung_4 (x0 , y0 , h, n , f):
    k=np.zeros(4)
    y=np.zeros(n+1)
    y[0]=y0

    for i in range (0 , n ):
        k[0]=y[i]
        k[1]=y[i]+(1/2)*h*calculate(x0+i*h , k[0] , f)
        k[2]=y[i]+(1/2)*h*calculate(x0+(i+1/2)*h, k[1] , f)
        k[3]= y[i] + h* calculate(x0+h*(i+1) , k[2], f)
        
        y[i+1] = y[i] + (1/6)* h *( calculate(x0+i*h , k[0] , f)  
                                   + 2* calculate(x0+(i+1/2)*h , k[1] , f) 
                                   + 2 * calculate(x0+(i+1/2)*h , k[2], f) 
                                   + calculate(x0+(i+1)*h , k[3] , f) )
        
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
rung_4(x, y, h, n, f)
input("Click Enter To Close.")


       