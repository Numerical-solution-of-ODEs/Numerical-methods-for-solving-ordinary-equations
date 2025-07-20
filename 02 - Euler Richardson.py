import numpy as np
from numpy import sin 
from numpy import cos 
from numpy import tan
from numpy import sinh
from numpy import cosh
from numpy import tanh

from matplotlib import pyplot as plt

def calculate(value1 , value2 , function):
    x = value1
    y = value2
    return eval(function)



def euler(x0 , y0 , h , n , f):
    y=np.zeros([n+1])
    y[0]=y0

    for i in range (0 , n):
         y[i+1]=y[i]+h*calculate(x0+h*i, y[i] , f)

    return y    
    

def eu_rich(x0 , y0 , h , n , f):
    y_h=euler(x0 , y0 , h , 2*n+3 , f)
    y_2h=euler(x0 , y0 , 2*h , n , f)

    y_hat = np.zeros(n+1)
    y_hat[0]=y0

    for i in range (0 ,n):
        y_hat[i+1]=2*y_h[2*(i+1)] - y_2h[i+1]
        print('y_richardson %i = %f' % (i+1, y_hat[i+1]))

    x=np.zeros(n+1)
    for i in range(0,n+1):
        x[i]=x0 + h * i
    

    plt.plot(x, y_hat, 'red')
    plt.plot(x,y_2h, 'green')
    plt.show()

f = str(input("If y'=f(x,y) , Please Enter f(x,y) : \n", ))
x = float(input("Please Enter x0 :\n"))
y = float(input("Please Enter y0 :\n"))
h = float(input("Please Enter Step Lenth (h) :\n"))
n = int(input("Please Enter Number Of Steps (n) : \n"))

eu_rich(x,y,h,n,f)
input("Click Enter To Close.")
